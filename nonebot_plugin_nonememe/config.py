from typing_extensions import TypedDict

from nonebot import get_plugin_config
from pydantic import BaseModel


class CronDict(TypedDict, total=False):
    year: str | int
    month: str | int
    day: str | int
    week: str | int
    day_of_week: str | int
    hour: str | int
    minute: str | int
    second: str | int


class ConfigModel(BaseModel):
    nonememe_proxy: str | None = None
    nonememe_repo_prefix: str = (
        "https://raw.githubusercontent.com/NoneMeme/NoneMeme/main"
    )

    nonememe_update_cron: CronDict = {"hour": "*/1"}
    nonememe_search_limit: int = 5


config = get_plugin_config(ConfigModel)
