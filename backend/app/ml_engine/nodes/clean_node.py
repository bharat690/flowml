import pandas as pd 
from pandas.api.types import is_numeric_dtype

def clean_dataset(file_path):
    df = pd.read_csv(file_path) 
    original_rows = len(df) 
    df = df.drop_duplicates() 
    rows_after_cleaning = len(df) 
    duplicates_removed = original_rows - rows_after_cleaning 
    missing_values = df.isnull().sum().to_dict()

    for column in df.columns:
      if is_numeric_dtype(df[column]):
         df[column] = df[column].fillna(df[column].median())
      else:
         df[column] = df[column].fillna(df[column].mode()[0])
    
    print(df.dtypes)

    return {
        "original_rows": original_rows,
        "duplicates_removed": duplicates_removed,
        "rows_after_cleaning": rows_after_cleaning,
        "missing_values" : missing_values
    }
        
