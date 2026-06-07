from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def test_workflow():
    return {"message": "Workflow route working"}