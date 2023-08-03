import json
import re
import urllib.parse
from pathlib import Path
from typing import List, cast

import anyio
import json5
from httpx import AsyncClient
from nonebot import get_driver, logger
from nonebot_plugin_apscheduler import scheduler
from pydantic import BaseModel, parse_raw_as

from .config import config

DATA_DIR = Path.cwd() / "data" / "nonememe"
LIST_CACHE_PATH = DATA_DIR / "cached_list.json"
MEME_CACHE_DIR = DATA_DIR / "cache"

if not MEME_CACHE_DIR.exists():
    MEME_CACHE_DIR.mkdir(parents=True)
# if MEME_CACHE_DIR.exists():
#     shutil.rmtree(MEME_CACHE_DIR)
# MEME_CACHE_DIR.mkdir(parents=True)


class MemeItem(BaseModel):
    name: str
    suffix: str
    path: str


meme_list: List[MemeItem] = []


def search_meme_items(
    keyword: str,
    use_regex: bool = False,  # noqa: FBT001
) -> List[MemeItem]:
    if use_regex:
        pattern = re.compile(keyword, re.I)
        return [item for item in meme_list if pattern.search(item.name)]

    kws = keyword.lower().split()
    matches = [
        (s, x)
        for x in meme_list
        if (s := len([kw for kw in kws if kw in x.name.lower()]))
    ]
    return [x[1] for x in sorted(matches, key=lambda x: x[0], reverse=True)]


async def fetch_meme(path: str) -> bytes:
    async with AsyncClient(proxies=config.nonememe_proxy) as cli:
        resp = await cli.get(f"{config.nonememe_repo_prefix}/{path}")
        return resp.content


async def get_meme(meme: MemeItem) -> bytes:
    cache_path = anyio.Path(MEME_CACHE_DIR / f"{meme.name}{meme.suffix}")
    if await cache_path.exists():
        return await cache_path.read_bytes()

    data = await fetch_meme(meme.path)
    await cache_path.write_bytes(data)
    return data


def build_meme_item(meme_path: str) -> MemeItem:
    path_obj = Path(urllib.parse.unquote(meme_path))
    return MemeItem(name=path_obj.stem, suffix=path_obj.suffix, path=meme_path)


async def fetch_meme_list() -> List[MemeItem]:
    async with AsyncClient(proxies=config.nonememe_proxy) as cli:
        resp = await cli.get(f"{config.nonememe_repo_prefix}/static/scripts/config.js")
        text = resp.text
        text = text[text.find("{") : text.rfind("}") + 1]

    items: List[str] = cast(dict, json5.loads(text))["items"]
    return [build_meme_item(item) for item in items]


async def update_meme_list():
    logger.info("Updating meme list")

    cache_json_path = anyio.Path(LIST_CACHE_PATH)

    try:
        got_meme_list = await fetch_meme_list()
        await cache_json_path.write_text(
            json.dumps(
                [x.dict() for x in got_meme_list],
                indent=2,
                ensure_ascii=False,
            ),
            encoding="u8",
        )

    except Exception:
        if not await cache_json_path.exists():
            raise

        logger.warning("Failed to fetch meme list, use cache instead")
        got_meme_list = parse_raw_as(
            List[MemeItem],
            await cache_json_path.read_text(encoding="u8"),
        )

    meme_list.clear()
    meme_list.extend(got_meme_list)
    logger.opt(colors=True).success(
        f"Succeed to update meme list, Loaded <y>{len(meme_list)}</y> memes",
    )


driver = get_driver()
driver.on_startup(update_meme_list)
scheduler.add_job(update_meme_list, "cron", **config.nonememe_update_cron)
