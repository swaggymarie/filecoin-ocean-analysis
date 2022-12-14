# %%
import matplotlib.pyplot as plt
import datetime
import numpy as np
import pandas as pd
import scipy.stats as stats

fig = plt.figure(figsize=(12, 8))

df = pd.read_csv(r'./datasets/FIL_price.csv')
df1 = pd.read_csv(r'./datasets/Filecoin_energy.csv')

df1["Date"] = df1["Date"].str[0:10]

start_date = df1.iloc[0].Date
end_date = df1.iloc[len(df1) - 1].Date

df = df.loc[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
# %%
fig , ax1 = plt.subplots()
ax2= ax1.twinx()
ax1.plot(df1.Date, df1["Data storage capacity"], color='blue')
ax2.plot(df1.Date, df1["Energy consumption rate estimate"], color='green')
ax2.set_ylim([0,400000])


r = stats.pearsonr(df1['Data storage capacity'], df1['Energy consumption rate estimate'])
print(r[0])

plt.xticks([df1['Date'][0], df1['Date'][len(df1['Date']) - 1]])
plt.show()

#%%
fig , ax1 = plt.subplots()
ax2= ax1.twinx()
ax1.plot(df1.Date, df1["Cumulative energy use estimate"], color='blue')
ax2.plot(df1.Date, df1["Energy consumption rate estimate"], color='green')
ax2.set_ylim([0,500000])


r = stats.pearsonr(df1['Cumulative energy use estimate'], df1['Energy consumption rate estimate'])
print(r[0])

plt.xticks([df1['Date'][0], df1['Date'][len(df1['Date']) - 1]])
plt.show()
# %%
fig , ax1 = plt.subplots()
ax2= ax1.twinx()
ax1.plot(df1.Date, df1["Cumulative energy use estimate"], color='blue', label="Energy use")
ax2.plot(df1.Date, df1["Cumulative renewable energy purchases"], color='green', label="Renewable energy purchases")
ax2.set_ylim([0,2500000000])
ax1.set_ylim([0,2500000000])

ax1.set_xlabel('Date')
ax1.legend()
ax2.legend()

plt.title("Total energy use vs renewable energy purchase")
plt.xticks([df1['Date'][0], df1['Date'][len(df1['Date']) - 1]])
plt.show()
#%%
fig , ax1 = plt.subplots()
ax1.plot(df1.Date,  df1["Cumulative renewable energy purchases"] / df1["Cumulative energy use estimate"], color='blue')
# ax2.plot(df1.Date, df1["Cumulative renewable energy purchases"], color='green')
# ax2.set_ylim([0,2500000000])
ax1.set_ylim([0,2])

ax1.set_xlabel('Date')
plt.title("Share of renewable energy")

plt.xticks([df1['Date'][0], df1['Date'][len(df1['Date']) - 1]])
plt.show()
#energy used to seal data
# %%
fig , ax1 = plt.subplots()
ax2= ax1.twinx()
ax1.plot(df.Date, df.Low, color='blue')
ax2.plot(df1.Date, df1["Energy used to seal data estimate"], color='green')
ax2.set_ylim([10,200000])

ax1.set_xlabel('Date')
ax1.set_ylabel('$FIL price', color='blue')
ax2.set_ylabel('energy used to seal the Filecoin data', color='green')
plt.xticks([df1['Date'][0], df1['Date'][len(df1['Date']) - 1]])
plt.show()

r = stats.pearsonr(df1['Energy used to seal data estimate'], df['Close'])
print(r[0])
r= stats.spearmanr(df1['Energy used to seal data estimate'], df['Close'])
print(r[0])

#data storage capacity
# %%
fig , ax1 = plt.subplots()
ax2= ax1.twinx()
ax1.plot(df.Date, df.Low, color='blue')
ax2.plot(df1.Date, df1["Data storage capacity added per day"], color='green')
ax2.set_ylim([0,150000000])

ax1.set_xlabel('Date')
ax1.set_ylabel('$FIL price', color='blue')
ax2.set_ylabel('Data storage capacity added per day', color='green')
plt.xticks([df1['Date'][0], df1['Date'][len(df1['Date']) - 1]])

plt.show()


r = stats.pearsonr(df1['Data storage capacity added per day'], df['Close'])
print(r[0])
r= stats.spearmanr(df1['Data storage capacity added per day'], df['Close'])
print(r[0])

#energy consumption rate
# %%
fig , ax1 = plt.subplots()
ax2= ax1.twinx()
ax1.plot(df.Date, df.Low, color='blue')
ax2.plot(df1.Date, df1["Energy consumption rate estimate"], color='green')
ax2.set_ylim([0,400000])
ax1.set_xlabel('Date')
ax1.set_ylabel('$FIL price', color='blue')
ax2.set_ylabel('Energy consumption rate', color='green')

plt.xticks([df1['Date'][0], df1['Date'][len(df1['Date']) - 1]])
plt.show()

r = stats.pearsonr(df1['Energy used to store data estimate'], df['Close'])
print(r[0])
r= stats.spearmanr(df1['Energy used to store data estimate'], df['Close'])
print(r[0])
# %%
