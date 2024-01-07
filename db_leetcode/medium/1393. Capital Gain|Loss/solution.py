import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    dd = {"stock_name": [], "capital_gain_loss": []}
    names = stocks["stock_name"].unique()
    for i in names:
        temp_df = stocks[stocks["stock_name"] == i].copy()
        temp_df = temp_df.sort_values("operation_day")
        value = 0
        for j in range(temp_df.shape[0]):
            if temp_df.iloc[j, 1] == "Buy":
                value -= temp_df.iloc[j, -1]
            else:
                value += temp_df.iloc[j, -1]
        dd["stock_name"] += [i]
        dd["capital_gain_loss"] += [value]
    
    return pd.DataFrame(dd)
