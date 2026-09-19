from http.client import HTTPException
from fastapi import APIRouter

router = APIRouter()


@router.get("/health", status_code=200)
def health():
    try:
        return {"status": "running"}
    except:
        raise HTTPException(status_code=500, detail="Internal server error")
