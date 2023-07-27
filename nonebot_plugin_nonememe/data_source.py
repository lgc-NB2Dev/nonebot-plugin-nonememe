import re
import urllib.parse
from dataclasses import dataclass
from pathlib import Path
from typing import List, cast

import json5
from httpx import AsyncClient
from nonebot import get_driver, logger

from .config import config


@dataclass
class MemeItem:
    name: str
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


def build_meme_item(meme_path: str) -> MemeItem:
    name = Path(urllib.parse.unquote(meme_path)).stem
    return MemeItem(name=name, path=meme_path)


async def fetch_meme_list() -> List[MemeItem]:
    async with AsyncClient(proxies=config.nonememe_proxy) as cli:
        resp = await cli.get(f"{config.nonememe_repo_prefix}/static/scripts/config.js")
        text = resp.text
        text = text[text.find("{") : text.rfind("}") + 1]

    items: List[str] = cast(dict, json5.loads(text))["items"]
    return [build_meme_item(item) for item in items]


async def init_meme_list():
    meme_list.clear()
    meme_list.extend(await fetch_meme_list())
    logger.opt(colors=True).success(
        f"Succeed to init meme list, Loaded <y>{len(meme_list)}</y> memes",
    )
    print(meme_list)


driver = get_driver()
driver.on_startup(init_meme_list)
