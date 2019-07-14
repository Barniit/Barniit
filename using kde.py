import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("C:\\Users\\Barnit\\Documents\\heatmap.csv")

df2=df.dropna(axis='columns',how='all')
lat=df2['longitude']
lon=df2['latitude']
wt=df2['weight']
df3=df2.drop('yrows',axis=1)
df3=df3.drop('xcols',axis=1)

ax=sns.kdeplot(lon,wt,kernel="gau",cmap="Blues",shade=True,shade_lowest=False)
ax.set_frame_on(True)

plt.show()
