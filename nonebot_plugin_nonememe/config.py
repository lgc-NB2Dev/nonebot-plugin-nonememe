from typing import Optional

from nonebot import get_driver
from pydantic import BaseModel


class ConfigModel(BaseModel):
    nonememe_proxy: Optional[str] = None
    nonememe_repo_prefix: str = (
        "https://raw.githubusercontent.com/NoneMeme/NoneMeme/main"
    )

    nonememe_search_limit: int = 5


config: ConfigModel = ConfigModel.parse_obj(get_driver().config.dict())
