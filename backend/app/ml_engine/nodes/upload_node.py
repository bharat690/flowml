# app/ml_engine/nodes/upload_node.py

def data_profile(df):
    return {
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": list(df.columns),
        "data_types": df.dtypes.astype(str).to_dict()
    }