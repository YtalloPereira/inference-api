from typing import Literal
from pydantic import BaseModel


class ResponseSchema(BaseModel):
    result: Literal[1,2,3]
