import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    pairs = dict()
    tivs = dict()
    _sum = 0
    for i in range(len(insurance)):
        one = insurance.iloc[i, -2]
        two = insurance.iloc[i, -1]
        tiv = insurance.iloc[i, 1]
        name = str(one) + "-" + str(two)
        if name in pairs:
            pairs[name] += 1
        else:
            pairs[name] = 1

        if tiv in tivs:
            tivs[tiv] += 1
        else:
            tivs[tiv] = 1
    for i in range(len(insurance)):
        tiv_cur = insurance.iloc[i, 2]
        tiv = insurance.iloc[i, 1]
        one = insurance.iloc[i, -2]
        two = insurance.iloc[i, -1]
        name = str(one) + "-" + str(two)
        if tivs[tiv] > 1 and pairs[name] == 1:
            _sum += tiv_cur
    
    dd = {'tiv_2016': round(_sum, 2)}
    return pd.DataFrame(dd, index=[0])
