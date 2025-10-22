import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    people = dict()
    companies = dict()
    for i in range(len(sales_person)):
        people[sales_person.iloc[i, 0]] = sales_person.iloc[i, 1]
    for i in range(len(company)):
        companies[company.iloc[i, 0]] = company.iloc[i, 1]
    
    orders["com_id"] = orders["com_id"].map(companies)
    orders["sales_id"] = orders["sales_id"].map(people)
    res = orders[orders["com_id"] == "RED"]["sales_id"].values
    dd = pd.DataFrame({"name": [i for i in sales_person["name"].values if i not in res]})
    return dd
