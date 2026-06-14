import pandas as pd 
from pandas.api.types import is_numeric_dtype

def clean_dataset(file_path):
    df = pd.read_csv(file_path) 
    original_rows = len(df) 
    df = df.drop_duplicates() 
    rows_after_cleaning = len(df) 
    duplicates_removed = original_rows - rows_after_cleaning 
    missing_values = df.isnull().sum().to_dict()
    outlier_report = {
        "checked" :[],
        "skipped" :{},
        "results": []
     }

    IDENTIFIER_PATTERNS = [
     "id",
     "_id",
     "_no",
     "code",
     "_code",
     "index",
     "key",
     "number"
    ]
    

    for column in df.columns:
      column_name = column.lower()
      if df[column].dtype == "str":
        converted = pd.to_numeric(
            df[column],
            errors="coerce"
        )

        success_rate = converted.notna().mean()

        if success_rate > 0.8:
            df[column] = converted

      is_identifier = False

      for pattern in IDENTIFIER_PATTERNS:
        if (column_name == pattern or column_name.endswith(pattern)):
           outlier_report["skipped"][column] = (
           f"identifier pattern: {pattern}"
           )
           is_identifier = True
           break

      if is_identifier:
        continue

  
      if is_numeric_dtype(df[column]):
         
         outlier_report["checked"].append(column)          

         df[column] = df[column].fillna(df[column].median())
         q1 = df[column].quantile(0.25) 
         q3 = df[column].quantile(0.75)
         iqr = q3 - q1 
         lower_bound = q1-1.5*iqr
         upper_bound = q3+1.5*iqr
         outlier_mask = ((df[column] < lower_bound )|(df[column] > upper_bound))
         outlier_rows = df[outlier_mask]
         df[column] = df[column].astype(float)
         median_value = df[column].median()
         for index,value in outlier_rows[column].items():
            outlier_report["results"].append(
                   {
                     "row_index": int(index),
                     "column": column,
                     "original_value": value,
                     "replacement_value": median_value
                   }
             ) 
    
         df.loc[outlier_mask,column] = median_value 
             
      else:
         df[column] = df[column].fillna(df[column].mode()[0])
         df[column] = df[column].str.strip().str.lower()
    

    return {
     "cleaned_df": df,
     "report": {
         "original_rows": original_rows,
         "duplicates_removed": duplicates_removed,
         "rows_after_cleaning": rows_after_cleaning,
         "missing_values": missing_values,
         "outliers": outlier_report
      }
    }
        
