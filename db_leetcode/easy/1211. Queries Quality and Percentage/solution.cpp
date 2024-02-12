import pandas as pd

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    queries["pos_rating"] = queries["rating"]/queries["position"]
    queries["quality"] = queries["rating"].apply(lambda x: 0 if x>=3 else 1)
    grouped = queries.groupby("query_name")
    means = pd.DataFrame(grouped["pos_rating"].mean())
    means.sort_index(inplace=True)
    means["pos_rating"] = means["pos_rating"].apply(lambda x: round(x, 2))
    quality = pd.DataFrame(grouped["quality"].mean())
    quality.sort_index(inplace=True)
    quality["quality"] = quality["quality"].apply(lambda x: round(x*100, 2))
    res = {"query_name": quality.index, "quality": means.iloc[:, 0].values,
            "poor_query_percentage": quality.iloc[:, 0].values}
    return pd.DataFrame(res)
