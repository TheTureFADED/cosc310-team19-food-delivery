from fastapi import FastAPI

from app.api.routes import health, restaurant_route




app = FastAPI(title="We will go through this sesemter like every other sesemter", version="0.0.0.0.1")

app.include_router(restaurant_route.router)
app.include_router(health.router)

@app.get("/")
def root():
    return {"message": "Backend is running"}
