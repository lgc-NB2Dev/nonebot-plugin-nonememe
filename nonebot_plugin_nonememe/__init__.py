from nonebot import require
from nonebot.plugin import PluginMetadata

require("nonebot_plugin_apscheduler")
require("nonebot_plugin_saa")

from . import __main__ as __main__  # noqa: E402
from .config import ConfigModel  # noqa: E402

__version__ = "0.2.0"
__plugin_meta__ = PluginMetadata(
    name="NoneMeme",
    description="NoneBot 群大佬的日常",
    usage=(
        "指令：`nonememe` / `nb草图` / `nb梗图`\n"
        "不带参数则随机选取一个，带上参数可以进行搜索，参数使用 `/` 开头及结尾使用正则表达式搜索"
    ),
    type="application",
    homepage="https://github.com/lgc-NB2Dev/nonebot-plugin-nonememe",
    config=ConfigModel,
    supported_adapters={
        "~onebot.v11",
        "~onebot.v12",
        "~kaiheila",
        "~qqguild",
        "~telegram",
        "~feishu",
        "~red",
    },
    extra={"License": "MIT", "Author": "student_2333"},
)
