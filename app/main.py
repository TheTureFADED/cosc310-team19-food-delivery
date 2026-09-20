from fastapi import FastAPI, HTTPException

from app.api.routes import restaurant_route

app = FastAPI(title="We will go through this sesemter like every other sesemter", version="0.0.0.0.1")

app.include_router(restaurant_route.router)

@app.get("/")
def root():
    return {"message": "Backend is running"}


@app.get("/health", status_code=200)
def health():
    try:
        return {"status": "ok"}
    except:
        raise HTTPException(status_code=500, detail="Internal server error")