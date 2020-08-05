import numpy as np
import pandas as pd
import baostock as bs

#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)
# 获取股票信息，返回集
rs = bs.query_history_k_data("000001.SH", "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST",
                             start_date='2010-01-01', end_date='2019-12-31', frequency="d", adjustflag="3")
# print('query_history_k_data respond error_code:'+rs.error_code)
# print('query_history_k_data respond  error_msg:'+rs.error_msg)
# 股票结果集封装DataFrome对象
dlist=[]
while (rs.error_code=='0')and rs.next():
    da=rs.get_row_data()
    # print(da)
    dlist.append(da)
df=pd.DataFrame(dlist)
print(df.head())
