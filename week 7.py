import numpy as np
import pandas as pd
import datetime
import pandas_datareader.data as web


start=datetime.datetime(2012,1,1)
end=datetime.datetime(2019,12,1)

tesla=web.DataReader('TSLA','yahoo',start,end)

tesla['profit']=tesla['Close']
tesla['Close'].shift(1)
tesla.loc[tesla['profit']>0,'Profitable']='Yes'

tesla['Profitable1']=np.where(tesla['profit']>0,'Yes','No')

tesla['Profitable']=tesla['profit']>0

tesla['Month']=tesla.index.month
tesla['Year']=tesla.index.year

df=tesla.groupby('Month')['profit','Profitable'].mean()
df=tesla.groupby(['Month','Year'])['profit'].mean()

temp1=df.reset_index()
temp1=df.unstack(level=0)

df=tesla.groupby('Month')['Close'].agg(lambda x:max(x)-min(x))
df=tesla.groupby(['Month','Year'])['Close'].agg(lambda x:max(x)-min(x))
df=df.unstack(level=0)

df=pd.pivot_table(tesla,index=['Month'])
df=pd.pivot_table(tesla,index=['Month','Year'])

df=pd.pivot_table(tesla,index=['Month','Year'],values=['Close'])
df=pd.pivot_table(tesla,index=['Month','Year'],values=['Close'],aggfunc=np.sum)
df=pd.pivot_table(tesla,index=['Month','Year'],values=['Close'],aggfunc=np.sum,fill_value=0)
df=pd.pivot_table(tesla,index=['Month','Year'],values=['Close'],aggfunc=np.sum,fill_value=0,margins=True)
df=pd.pivot_table(tesla,index=['Year'],values=['Close'],columns=['Month'],aggfunc=np.sum,fill_value=0,margins=True)


tesla['moving average']=tesla['Close'].rolling(window=3).mean()
tesla.to_excel('tesla.xlsx')







data=pd.DataFrame([[1.,6.5,3.],[1.,np.nan,np.nan],[np.nan,np.nan,np.nan],[np.nan,2.5,9.]])
data.dropna()
data.dropna(how='all')
data[4]=np.nan
data.dropna(axis=1,how='all')
data.dropna(thresh=2)
data.fillna(0)
data.fillna({1:0.5,2:0,4:9})
data.fillna(method='ffill',limit=1)
data.fillna(method='bfill')
data.fillna(data.mean())



data=pd.DataFrame({'k1':['one','two']*3+['two'],'k2':[1,1,2,3,3,4,4]})
data.duplicated()
data.drop_duplicates()
data['v1']=range(7)
data.drop_duplicates(['k1'])
data.drop_duplicates(['k1','k2'],keep='last')






iris=pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
import seaborn as sns
















