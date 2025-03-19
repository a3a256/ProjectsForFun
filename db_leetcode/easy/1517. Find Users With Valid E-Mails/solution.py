import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    alp = "abcdefghijklmnopqrstuvwxyz0123456789_-."
    dd = {"user_id": [], "name": [], "mail": []}
    for i, j in enumerate(users["mail"].values):
        if j.endswith("@leetcode.com"):
            check = True
            pos = j.find("@leetcode.com")
            for k in j[:pos].lower():
                if k not in alp:
                    check = False
            if j[0].lower() not in alp[:26]:
                check = False
            if check:
                dd["user_id"] += [users.iloc[i, 0]]
                dd["name"] += [users.iloc[i, 1]]
                dd["mail"] += [j]

    return pd.DataFrame(dd)
