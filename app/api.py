from fastapi import FastAPI
from router.metrics import router
app = FastAPI(
    title="My FastAPI Application",
    description="This is a sample FastAPI application.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)
@app.get("/")
def say():
    """
    this is api for testing purpose
    """
    return {"message": "welcome to api learning Aliya"}

app.include_router(router)