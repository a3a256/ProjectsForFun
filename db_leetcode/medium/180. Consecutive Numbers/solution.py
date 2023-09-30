import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    vals = []
    log = dict()
    for i in logs["num"]:
        if i not in log:
            if len(log) > 0:
                log = dict()
            log[i] = 1
        else:
            log[i] += 1

        if log[i] >= 3:
            if i not in vals:
                vals += [i]

    return pd.DataFrame({"ConsecutiveNums": vals})
