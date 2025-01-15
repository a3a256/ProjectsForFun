import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    counts = my_numbers["num"].value_counts()
    nums = []
    for i, j in enumerate(counts):
        if j == 1:
            nums += [counts.index[i]]

    if len(nums) == 0:
        nums = [np.nan]
    else:
        nums = [max(nums)]
    return pd.DataFrame({"num": nums})
