import pandas as pd
import datetime
import time
import matplotlib.pyplot as plt


df = pd.read_csv("out_usd.csv")
df['ndate']=pd.to_datetime(df['date'].values*1000000000)
ndf=df.sort_values('ndate')
plt.plot(ndf['ndate'],ndf['price'])

plt.show()
