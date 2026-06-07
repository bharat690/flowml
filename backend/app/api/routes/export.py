from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def test_export():
    return {"message": "Export route working"}