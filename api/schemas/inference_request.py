from pydantic import BaseModel

class RequestSchema(BaseModel):
    no_of_adults :int
    no_of_children :int
    required_car_parking_space: int
    lead_time :int
    arrival_year :int
    arrival_month :int
    arrival_date :int
    type_of_meal_plan :object
    room_type_reserved :object
    market_segment_type :object
    no_of_special_requests :int