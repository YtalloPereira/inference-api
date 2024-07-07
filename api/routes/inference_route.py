from fastapi import APIRouter, HTTPException
from api.schemas.inference_request import RequestSchema
from api.schemas.inference_response import ResponseSchema

router = APIRouter()

@router.post("/api/v1/inference", response_model=ResponseSchema)
async def run_inference(request: RequestSchema):
    try:
       
        #implementar lógica de inferencia
        result = 1  

       
        return ResponseSchema(result=result)
    
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Erro durante a inferência: {str(err)}")