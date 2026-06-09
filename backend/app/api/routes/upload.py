from fastapi import UploadFile,APIRouter, File 
import os 
import pandas as pd
from app.ml_engine.nodes.upload_node import data_profile

router  = APIRouter()
UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok = True ) 

@router.post("/")
async def upload_csv(file:UploadFile = File(...)):
      if not file.filename.endswith(".csv"):
          return {"error": "Please upload a CSV file"}
      
      file_path = os.path.join(UPLOAD_FOLDER,file.filename) 
      
      with open(file_path,"wb")as buffer:
          buffer.write(await file.read())
      df = pd.read_csv(file_path) 
      profile = data_profile(df)
      return {
        "filename": file.filename,
        "profile" : profile
      }
          