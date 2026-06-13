from fastapi import APIRouter , HTTPException
from app.ml_engine.nodes.clean_node import clean_dataset 
import os 
from app.core.config import settings
from app.core.session import sessions

router = APIRouter() 

@router.post("/")
async def clean_csc(session_id : str ) : 
       
       if session_id not in sessions:
        raise HTTPException(
             status_code = 404 , 
             detail = "session not found"
        )
       file_path = sessions[session_id]["file_path"]

       if not os.path.exists(file_path):
        raise HTTPException(
             status_code = 404,
             detail = "file not found"
        )

       result = clean_dataset(file_path)
       sessions[session_id]["clean_report"] = result
       return result 
          