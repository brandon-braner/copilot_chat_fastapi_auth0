from fastapi import FastAPI
from app.api.routes import router as api_router

app = FastAPI()

@app.on_event("startup")
async def startup():
    # Add startup events here
    pass

@app.on_event("shutdown")
async def shutdown():
    # Add shutdown events here
    pass

app.include_router(api_router, prefix="/api")