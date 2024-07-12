from fastapi import APIRouter, HTTPException
from schemas.inference_request import RequestSchema
from schemas.inference_response import ResponseSchema
from utils.inference_script import make_inference
from pydantic import ValidationError

router = APIRouter()


@router.post("/api/v1/inference", response_model=ResponseSchema)
async def run_inference(request: RequestSchema):
    try:
        input_data = request.model_dump()

        result = make_inference(input_data)

        return ResponseSchema(result=result)
    except ValidationError as ve:
        raise HTTPException(status_code=422, detail=f"Validation error: {str(ve)}")
    except Exception as err:
        raise HTTPException(
            status_code=500, detail=f"Error during inference: {str(err)}"
        )
