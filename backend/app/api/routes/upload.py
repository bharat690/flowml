from fastapi import UploadFile,APIRouter, File 
import os 
import pandas as pd

router  = APIRouter()
UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok = True ) 

def data_profile(df):
    return{
        "rows" : len(df),
        "columns" : len(df.columns),
        "column_names" : list(df.columns),
        "data_types":df.dtypes.astype(str).to_dict()   
    }
    

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
          