from typing import Optional, Union
from typing_extensions import TypedDict

from nonebot import get_plugin_config
from pydantic import BaseModel


class CronDict(TypedDict, total=False):
    year: Union[str, int]
    month: Union[str, int]
    day: Union[str, int]
    week: Union[str, int]
    day_of_week: Union[str, int]
    hour: Union[str, int]
    minute: Union[str, int]
    second: Union[str, int]


class ConfigModel(BaseModel):
    nonememe_proxy: Optional[str] = None
    nonememe_repo_prefix: str = (
        "https://raw.githubusercontent.com/NoneMeme/NoneMeme/main"
    )

    nonememe_update_cron: CronDict = {"hour": "*/1"}
    nonememe_search_limit: int = 5


config = get_plugin_config(ConfigModel)
