import pandas as pd
import matplotlib.pyplot as plt
from plot import Plotting

df = pd.read_csv(r'CC GENERAL.csv')
numerical = ['BALANCE', 'PURCHASES', 'ONEOFF_PURCHASES', 'INSTALLMENTS_PURCHASES', 'CASH_ADVANCE', 'CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_TRX', 'PURCHASES_TRX', 'CREDIT_LIMIT', 'PAYMENTS', 'MINIMUM_PAYMENTS', 'PRC_FULL_PAYMENT']
pp = Plotting(df, vars=numerical).plot()