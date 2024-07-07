from pydantic import BaseModel

class ResponseSchema(BaseModel):
    result: int