import datetime

d=datetime.datetime.now()
print(d)

d=datetime.date.today()
print(d)
dir(datetime)

d=datetime.date(2019,4,13)
str(d)
from datetime import date

d=date(2019,4,13)
d.month
d.year
d.day

from datetime import time
a=time()
print(a)
print("a=",a)
b=time(11,34,56)
print("b =",b)
c=time(hour=11,minute=34,second=56)
print("c =",c)
a=time(11,34,56)
a.hour

from datetime import datetime
a=datetime(2017,11,28,23,55,59,342380)
print("year=",a.year)
print("month =",a.month)
print("hour =",a.hour)
print("minute =",a.minute)
print("seconds =",a.second)
print("timestamp =",a.timestamp)

t4=datetime(year=2019,month=1,day=12,hour=7,minute=9,second=13)
t5=datetime(year=2021,month=1,day=12,hour=7,minute=9,second=13)
t6=t5-t4
print("t6 =",t6)

now=datetime.now()
t=now.strftime("%H:%M:%S")
print("time:",t)

s1=now.strftime("%d/%m/%Y,%H:%M:%S")
print("s1 =",s1)

s2=now.strftime("%d/%m/%Y,%H:%M:%S")
print("s2 =",s2)

#_________________________________________________________________#
import pandas as pd
s=pd.Series()

s=pd.Series(range(0,5),index=['a','b','c','d','e'])

s[0]
s[-1]
s[-3:]
s['a']

data={'01':'BATMAN','04':'FLASH','07':'IRON MAN','09':'SPIDER-MAN'}
s=pd.Series(data)

s=pd.Series(data,index=['07','04','01','09'])
s=pd.Series(data,index=['01','04','01','09'])
s=pd.Series(data,index=['02','04','01','09'])


s.isna()
any(s.isna())
s.dropna(inplace=True)
s.fillna(0)
s=s.fillna('BATMAN')


data={'Year':[2000,2005,2010,2015],
      'Median Age':[24,56,40,20],
      'Height':[5.6,6.7,7.8,8.9]}

df=pd.DataFrame(data)
df=pd.DataFrame(data,columns=['Year','Height','Median Age'])
df=df.set_index('Year')
df.reset_index()
df.Height
df['Height']

df.index
df['m/h']=df['Median Age']/df['Height']
df['m/h']>7
df[df['m/h']>7]
df[df['m/h']>7].index

df.loc[2000]
df.iloc[0]
df['Height'][2000]

df.idxmax()
df.idxmin()

df.describe()
df.count()
df.mean()
df.max()
df.min()
df.std()
df.var()
df.median()

df1=df.T

df2=pd.DataFrame([[50,51,52],[53,54,55],[56,57,58]])
df2=df2.T

df3=pd.DataFrame([[1,2,3,4],[5,6,7,8]])
df4=df2+df3
df5=df2.add(df3,fill_value=0)

df3.replace(3,9,inplace=True)

a=pd.to_datetime('4th of July 2019')
print(a)
a=pd.to_datetime('12.01.2019')
a=pd.to_datetime('12/01/2019')
a=pd.to_datetime('12-Jan-2019')
a=pd.to_datetime('12Jan2019')
a=pd.to_datetime('12.01.2019',dayfirst=True)
a=pd.to_datetime('12.01.2019',dayfirst=False)
?pd.to_datetime

a=pd.date_range(start='2017-01-01',end='2019-01-01')
a=pd.date_range(start='2017-01-01',end='2019-01-01',freq='M')
a=pd.date_range(start='2017-01-01',periods=0,freq='M')



#____________________________________________________________#
#TO INSTALL ANY PACKAGE
conda install -c anaconda pandas-datareader

import numpy as np
import pandas as pd
import datetime
import pandas_datareader.data as web


start=datetime.datetime(2012,1,1)
end=datetime.datetime(2019,12,1)

tesla=web.DataReader('TSLA','yahoo',start,end)
ford=web.DataReader('F','yahoo',start,end)
gm=web.DataReader('GM','yahoo',start,end)


#   temp=pd.read_csv('TSLA.csv')


tesla.loc['2017-03-06','High']
tesla1=tesla[['High','Low']]
tesla1=tesla[['Volume','High','Low']]
tesla1.columns=['A','B','C']

new=tesla.append(ford)
new=tesla.append(ford,ignore_index=True)


tesla['TOTAL TRADED']=tesla['Open']
tesla['Volume']


#CONCAT
car_comp=pd.concat([tesla['Open'],gm['Open'],ford['Open']],axis=1)
car_comp.columns=['Tesla Open','GM Open','Ford Open']
car_comp=pd.concat([tesla['Open'],gm['Open'],ford['Open']],axis=1,keys=['Tesla','GM','Ford'])

tesla=web.DataReader('TSLA','yahoo',datetime.datetime(2017,1,1),datetime.datetime(2019,12,1))
gm=web.DataReader('GM','yahoo',datetime.datetime(2016,1,1),datetime.datetime(2018,12,1))

car_comp=pd.merge(tesla['Open'],gm['Open'],left_index=True,right_index=True)

car_comp=pd.merge(tesla['Open'],gm['Open'],left_index=True,right_index=True,suffixes=("_tesla","_gm"),how='inner')

#subtract with one value below, 1st value will be nan
tesla['profit']=tesla['Close']-tesla['Close'].shift(1)
tesla['temp']=tesla['Close'].shift(1)
tesla['returns']=tesla['Close'].pct_change(1)


