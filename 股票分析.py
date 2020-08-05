import tushare as ts
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
#1 股票代码、起止日期可替换, 返回DataFrame对象自动使用时间作为索引对象，名称date
caixin = ts.get_hist_data('600633', start='2017-07-01', end='2020-05-08')
nan=ts.get_hist_data('601900', start='2017-07-01', end='2020-05-08')

# 为了绘制折线图，创建特殊结构DataFrame对象
#             浙江传媒财新
# date
# 2020-05-08    9.76
# print(caixin.index)
#2 caixin.close--Series对象  ：使用名称date作为索引
data = {'浙江传媒财新': caixin.close,'南方传媒':nan.close}
df=pd.DataFrame(data)
print(df)
df.sort_values(by='date',ascending=True,inplace=True)
# print(type(df.iloc[:,0]),df.iloc[:,0].index,df.iloc[:,0])
# 3 使用带有日期索引的DataFrame自动绘制折线图（图形自动优化）
df.plot(kind='line')
# plt.plot(df.iloc[:,0].index,df.iloc[:,0])
plt.show()