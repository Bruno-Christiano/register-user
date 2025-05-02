from pydantic import BaseModel
from typing import Optional


class ErrorMessage(BaseModel):
    message: str
    description: Optional[str] = None

    class Config:
        exclude_none = True
