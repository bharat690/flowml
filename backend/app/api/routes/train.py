from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def test_train():
    return {"message": "Train route working"}