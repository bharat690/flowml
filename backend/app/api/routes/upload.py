from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def test_upload():
    return {"message": "Upload route working"}