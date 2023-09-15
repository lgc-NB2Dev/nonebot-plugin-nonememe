from typing import Optional, Union
from typing_extensions import NotRequired, TypedDict

from nonebot import get_driver
from pydantic import BaseModel


class CronDict(TypedDict):
    year: NotRequired[Union[str, int]]
    month: NotRequired[Union[str, int]]
    day: NotRequired[Union[str, int]]
    week: NotRequired[Union[str, int]]
    day_of_week: NotRequired[Union[str, int]]
    hour: NotRequired[Union[str, int]]
    minute: NotRequired[Union[str, int]]
    second: NotRequired[Union[str, int]]


class ConfigModel(BaseModel):
    nonememe_proxy: Optional[str] = None
    nonememe_repo_prefix: str = (
        "https://raw.githubusercontent.com/NoneMeme/NoneMeme/main"
    )

    nonememe_update_cron: CronDict = {"hour": "*/1"}
    nonememe_search_limit: int = 5


config: ConfigModel = ConfigModel.parse_obj(get_driver().config.dict())
