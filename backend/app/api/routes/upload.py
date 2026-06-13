from fastapi import UploadFile,APIRouter, File ,HTTPException
import os 
import pandas as pd
from app.ml_engine.nodes.upload_node import data_profile
from app.core.config import settings

router  = APIRouter()

os.makedirs(settings.UPLOAD_FOLDER, exist_ok = True ) 

@router.post("/")
async def upload_csv(file:UploadFile = File(...)):
      if not file.filename.endswith(".csv"):
          raise HTTPException(
                status_code = 400,
                detail = "please upload a csv file"
          )
      
      file_path = os.path.join(settings.UPLOAD_FOLDER,file.filename) 
      
      with open(file_path,"wb")as buffer:
          buffer.write(await file.read())
      df = pd.read_csv(file_path) 
      profile = data_profile(df)
      return {
        "filename": file.filename,
        "profile" : profile
      }
          