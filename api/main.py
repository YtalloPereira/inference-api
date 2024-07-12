from fastapi import FastAPI
from routes.inference_route import router as api_router

app = FastAPI(
    title="Inference API",
    description="API to run inference from the model trained in SageMaker using the XGBoost framework and hotel reservations dataset from kaggle.com",
    version="1.0.0",
)

app.include_router(api_router, tags=["Inference"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
