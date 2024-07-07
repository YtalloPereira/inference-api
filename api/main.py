from fastapi import FastAPI
from api.routes import inference_route

app = FastAPI()

app.include_router(inference_route.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)