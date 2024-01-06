import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    unique_ids = customer["customer_id"].unique()
    full = []
    for i in unique_ids:
        temp = customer[customer["customer_id"] == i]["product_key"].nunique()
        if temp == len(product):
            full += [i]
    
    return pd.DataFrame({"customer_id": full})
