from fastapi import APIRouter , HTTPException
from app.ml_engine.nodes.clean_node import clean_dataset 
import os 
from app.core.config import settings

router = APIRouter() 

@router.post("/")
async def clean_csc(filename : str ) : 
       file_path = os.path.join(settings.UPLOAD_FOLDER, filename)
       if not os.path.exists(file_path):
        raise HTTPException(
             status_code = 404,
             detail = "file not found"
        )

       result = clean_dataset(file_path)

       return result 
          