from fastapi import APIRouter
from app.ml_engine.nodes.clean_node import clean_dataset 
import os 

UPLOAD_FOLDER = "uploads" 

router = APIRouter() 

@router.post("/")
async def clean_csc(filename : str ) : 
       file_path = os.path.join(UPLOAD_FOLDER, filename)
       if not os.path.exists(file_path):
        return {"error": "File not found"}

       result = clean_dataset(file_path)

       return result 
          