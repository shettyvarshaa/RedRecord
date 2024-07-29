from typing import List

from pydantic import BaseModel


class Session(BaseModel):
    transcript: str


class PreviousContent(BaseModel):
    contentList: List[str]
