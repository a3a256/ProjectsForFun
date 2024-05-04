import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    dd = {"id": [], "type": []}

    for i in range(tree.shape[0]):
        index = tree.iloc[i, 0]
        dd["id"] += [index]
        if pd.isna(tree.iloc[i, 1]):
            dd["type"] += ["Root"]
            continue
        if index in tree["p_id"].values:
            dd["type"] += ["Inner"]
        else:
            dd["type"] += ["Leaf"]

    return pd.DataFrame(dd)
