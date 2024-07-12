from fastapi import APIRouter, HTTPException
from schemas.inference_request import RequestSchema
from schemas.inference_response import ResponseSchema
from utils.inference_script import make_inference
from pydantic import ValidationError

router = APIRouter()

@router.post("/api/v1/inference", response_model=ResponseSchema)
async def run_inference(request: RequestSchema):
    try:
        input_data = [[
            request.no_of_adults,
            request.no_of_children,
            request.required_car_parking_space,
            request.lead_time,
            request.arrival_year,
            request.arrival_month,
            request.arrival_date,
            request.type_of_meal_plan,
            request.room_type_reserved,
            request.market_segment_type,
            request.no_of_special_requests
        ]]

        result = make_inference(input_data)
        return ResponseSchema(result=result)
    except ValidationError as ve:
       raise HTTPException(status_code=422, detail=f"Erro de validação: {str(ve)}")
    except Exception as err:
       raise HTTPException(status_code=500, detail=f"Erro durante a inferência: {str(err)}")