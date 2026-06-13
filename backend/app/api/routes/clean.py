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
       cleaned_path = os.path.join(settings.UPLOAD_FOLDER,"cleaned",os.path.basename(file_path))

       result = clean_dataset(file_path)
       cleaned_df = result["cleaned_df"]
       cleaned_df.to_csv(cleaned_path,index = False)
       report = result["report"]
       sessions[session_id]["clean_report"] = report
       sessions[session_id]["steps_run"].append("clean")
       sessions[session_id]["cleaned_path"] = cleaned_path
       
       return report
          