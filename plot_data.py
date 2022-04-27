import csv
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt


# A parser is required to translate the timestamp
custom_date_parser = lambda x: datetime.strptime(x, '%d-%m-%Y %H:%M_%S.%f')
#custom_date_parser = lambda x: pd.to_datetime(x).strftime("%d-%m-%Y_%H:%M_%S.%f")

df1 = pd.read_csv(
'~/Downloads/Fluorometer/Trial_3/24-04-22/24-04-2022_05_00.csv',
parse_dates=['Timestamp'], date_parser=custom_date_parser)
#x3 = df7['Timestamp']
y1 = df1['Mean_values']

df2 = pd.read_csv(
'~/Downloads/Fluorometer/Trial_3/25-04-22/25-04-2022_05_00.csv',
parse_dates=['Timestamp'], date_parser=custom_date_parser)
#x2 = df6['Timestamp']
y2 = df2['Mean_values']

df3 = pd.read_csv(
'~/Downloads/Fluorometer/Trial_3/26-04-22/26-04-2022_05_00.csv',
parse_dates=['Timestamp'], date_parser=custom_date_parser)
#x2 = df7['Timestamp']
y3 = df3['Mean_values']

plt.plot(y1, 'g',linewidth=5, alpha=0.3, label='24 Apr')
plt.plot(y2, 'r',linewidth=2, label='25 Apr')
plt.plot(y3, 'b', linewidth=1, label='26 Apr')
#plt.plot(y6, 'r', linewidth=3, alpha=0.3)
#plt.plot(y7, 'b', linewidth=1)
plt.grid()
plt.legend()
plt.show()
