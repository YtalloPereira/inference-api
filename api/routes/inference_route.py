from fastapi import APIRouter, HTTPException
from api.schemas.inference_request import RequestSchema
from api.schemas.inference_response import ResponseSchema

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
        #baixar model via s3 e usá-lo aqui
        #prediction = model.predict(input_data)
        ##result = 1  

        #return ResponseSchema(result=int(prediction[0]))
      
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Erro durante a inferência: {str(err)}")