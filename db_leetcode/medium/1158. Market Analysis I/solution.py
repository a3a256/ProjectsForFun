import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    mp = dict()
    for i in range(orders.shape[0]):
        _id = orders.iloc[i, -2]
        year = orders.iloc[i, 1].year
        if year == 2019:
            if _id not in mp:
                mp[_id] = 1
            else:
                mp[_id] += 1

    dd = {"buyer_id": [], "join_date": [], "orders_in_2019": []}
    for i, j in enumerate(users["user_id"].values):
        dd["buyer_id"] += [j]
        dd["join_date"] += [users.iloc[i, 1]]
        if j not in mp:
            dd["orders_in_2019"] += [0]
        else:
            dd["orders_in_2019"] += [mp[j]]

    return pd.DataFrame(dd)
