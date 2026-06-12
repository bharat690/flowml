import pandas as pd 

def clean_dataset(file_path):
    df = pd.read_csv(file_path) 
    original_rows = len(df) 
    df = df.drop_duplicates() 
    rows_after_cleaning = len(df) 
    duplicates_removed = original_rows - rows_after_cleaning 
    return {
        "original_rows": original_rows,
        "duplicates_removed": duplicates_removed,
        "rows_after_cleaning": rows_after_cleaning
        import pandas as pd 

def clean_dataset(file_path):
    df = pd.read_csv(file_path) 
    original_rows = len(df) 
    df = df.drop_duplicates(df) 
    rows_after_cleaning = len(df) 
    duplicates_removed = original_rows - rows_after_cleaning 
    missing_values = df.isnull().sum().to_dict()
    return {
        "original_rows": original_rows,
        "duplicates_removed": duplicates_removed,
        "rows_after_cleaning": rows_after_cleaning,
        "missing_values" :  missing_values
    }