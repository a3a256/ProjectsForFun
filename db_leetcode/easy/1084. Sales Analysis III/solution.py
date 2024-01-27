import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    mp = dict()
    for i in range(product.shape[0]):
        mp[product.iloc[i, 0]] = product.iloc[i, 1]
    qp = dict()
    for i in range(sales.shape[0]):
        if sales.iloc[i, 1] not in qp:
            qp[sales.iloc[i, 1]] = [sales.iloc[i, 3]]
        else:
            qp[sales.iloc[i, 1]] += [sales.iloc[i, 3]]

    
    dd = {"product_id": [], "product_name": []}
    for i, j in qp.items():
        year = j[-1].year
        month = j[-1].month
        day = j[-1].day
        if year == 2019:
            if month>=1 and month<=3:
                if day>=1 and day<=31:
                    dd["product_id"] += [i]
                    dd["product_name"] += [mp[i]]
        
    return pd.DataFrame(dd)
