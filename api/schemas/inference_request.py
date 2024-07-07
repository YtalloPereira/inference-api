from pydantic import BaseModel

class RequestSchema(BaseModel):
    no_of_adults: int
    no_of_children: int
    type_of_meal_plan: str