from pydantic import BaseModel
from typing import Literal


class RequestSchema(BaseModel):
    no_of_adults: int
    no_of_children: int
    required_car_parking_space: int
    lead_time: int
    arrival_year: int
    arrival_month: int
    arrival_date: int
    type_of_meal_plan: Literal[
        "Meal Plan 1", "Meal Plan 2", "Meal Plan 3", "Not Selected"
    ]
    room_type_reserved: Literal[
        "Room_Type 1",
        "Room_Type 2",
        "Room_Type 3",
        "Room_Type 4",
        "Room_Type 5",
        "Room_Type 6",
        "Room_Type 7",
    ]
    market_segment_type: Literal[
        "Aviation", "Complementary", "Corporate", "Offline", "Online"
    ]
    no_of_special_requests: int
