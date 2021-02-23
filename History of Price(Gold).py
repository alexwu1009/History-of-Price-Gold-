import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn; seaborn.set()

df = pd.read_html('https://rate.bot.com.tw/gold/chart/year/TWD')
df = df[0]
df.index = pd.to_datetime(df['日期'])
#製作買入表格
df1 = df[['日期','本行買入價格']]

#製作賣出表格
df2 = df[['日期', '本行賣出價格']]

#平均值
avg = df1['本行買入價格'].mean()
avg2 = df2['本行賣出價格'].mean()

print('========================== 作圖1 ==========================‘)

#買入表格
plt.subplots(figsize=(10, 5))
plt.plot(df1['本行買入價格'], label='BUY')
plt.axhline(y = avg, color='blue', ls='--', alpha=0.3, label='buy_avg')

plt.fill_between(df1.index, avg, df1['本行買入價格'],
                 where=df1['本行買入價格']>=avg, color='gray',
                 alpha=0.5, interpolate=True)

plt.title('History of Taiwan Bank Gold Price(BUY)')
plt.xlabel('DATE')
plt.ylabel('DOLLARS')
plt.legend(facecolor='white')

print('========================== 作圖2 ==========================‘)

#賣出表格
plt.subplots(figsize=(10, 5))
plt.plot(df2['本行賣出價格'], label='SOLD', color='orange')
plt.axhline(y = avg2, color='orange', ls='--', alpha=0.3, label='sold_avg')

plt.fill_between(df2.index, avg2, df2['本行賣出價格'],
                 where=df2['本行賣出價格']>=avg2, color='gray',
                 alpha=0.5, interpolate=True)

plt.title('History of Taiwan Bank Gold Price(SOLD)')
plt.xlabel('DATE')
plt.ylabel('DOLLARS')
plt.legend(facecolor='white')
plt.show()

print('========================== 作圖3 ==========================‘)

#表格合併
plt.subplots(figsize=(10, 5))
plt.plot(df1['本行買入價格'], label='BUY')
plt.axhline(y = avg, color='blue', ls='--', alpha=0.3, label='buy_avg')
plt.plot(df2['本行賣出價格'], label='SOLD')
plt.axhline(y = avg2, color='orange', ls='--', alpha=0.3, label='sold_avg')

plt.xlabel('DATE')
plt.ylabel('DOLLARS')
plt.title('History of Taiwan Bank Gold Price')
plt.legend(facecolor='white')
plt.show()
