import random
from typing import NoReturn

from nonebot import logger, on_command
from nonebot.adapters import Event, Message
from nonebot.exception import FinishedException
from nonebot.matcher import Matcher
from nonebot.params import CommandArg
from nonebot.typing import T_State
from nonebot_plugin_alconna.uniseg import UniMessage

from .config import config
from .data_source import MemeItem, get_meme, meme_list, search_meme_items


async def finish_with_meme(meme_item: MemeItem) -> NoReturn:
    try:
        image_bytes = await get_meme(meme_item)
    except Exception as e:
        logger.exception("Failed to get meme")
        await UniMessage("获取图片失败，请检查后台日志").send()
        raise FinishedException from e
    await (
        UniMessage.text(f"# {meme_item.name}")
        .image(raw=image_bytes)
        .send(reply_to=True)
    )
    raise FinishedException


cmd_meme = on_command("nonememe", aliases={"nb草图", "nb梗图"})


@cmd_meme.handle()
async def _(matcher: Matcher, state: T_State, arg_msg: Message = CommandArg()):
    arg = arg_msg.extract_plain_text().strip()
    if not arg:
        await finish_with_meme(random.choice(meme_list))

    use_regex = arg.startswith("/") and arg.endswith("/")
    if use_regex:
        arg = arg[1:-1]

    searched = search_meme_items(arg, use_regex=use_regex)
    if not searched:
        await matcher.finish("没有找到相关图片")
    if len(searched) == 1:
        await finish_with_meme(searched[0])

    over_length = len(searched) > config.nonememe_search_limit
    if over_length:
        searched = searched[: config.nonememe_search_limit]
    state["items"] = searched

    list_text = "\n".join(f"{i }. {item.name}" for i, item in enumerate(searched, 1))
    over_len_tip = (
        f"\nTip：搜索到的结果过多，仅显示前 {config.nonememe_search_limit} 条"
        if over_length
        else ""
    )
    await matcher.pause(f"找到多张图片，请发送序号选择：\n{list_text}{over_len_tip}")


@cmd_meme.handle()
async def _(matcher: Matcher, state: T_State, event: Event):
    arg = event.get_plaintext().strip()
    if arg in ("0", "q", "quit", "exit", "退出"):
        await matcher.finish("已退出选择")

    searched: list[MemeItem] = state["items"]
    if not (arg.isdigit() and (0 <= (index := (int(arg) - 1)) < len(searched))):
        await matcher.reject("请输入正确的结果序号，退出选择请发送 `0`")

    await finish_with_meme(searched[index])
