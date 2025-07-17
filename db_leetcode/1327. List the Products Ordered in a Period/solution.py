import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    dd = dict()
    for i in range(len(orders)):
        date = orders.iloc[i, 1]
        if str(date).startswith("2020-02-"):
            print(orders.iloc[i, 0])
            if orders.iloc[i, 0] not in dd:
                dd[orders.iloc[i, 0]] = orders.iloc[i, -1]
            else:
                dd[orders.iloc[i, 0]] += orders.iloc[i, -1]
    dt = {"product_name": [], "unit": []}
    for i, j in dd.items():
        if j >= 100:
            dt["product_name"] += [products[products["product_id"] == i]["product_name"].values[0]]
            dt["unit"] += [j]
    return pd.DataFrame(dt)
