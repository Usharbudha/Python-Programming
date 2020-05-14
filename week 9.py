import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,2*np.pi,400)
y=np.sin(x**2)
'''
fig,ax=plt.subplots()
ax.plot(x,y)
ax.set_title('A Single Plot')
plt.show()

fig,axs=plt.subplots(2)
fig.suptitle("Vertically Stacked Subplots")
axs[0].plot(x,y)
axs[1].plot(-x,y)
plt.show()
'''

plt.subplot(2,1,1)
plt.plot(x,y)
plt.ylabel("Chart 1")

plt.subplot(2,1,2)
plt.plot(x,-y)
plt.ylabel("Chart 2")

plt.subplot(3,1,3)
plt.plot(-x,y)
plt.ylabel("Chart 3")

plt.subplot(4,1,4)
plt.plot(-x,-y)
plt.ylabel("Chart 4")

plt.show()

fig,((ax1,ax2),(ax3,ax4))=plt.subplots(2,2)
fig.suptitle('Sharing x per column, y per row')
ax1.plot(x,y)
ax2.plot(x,y**2,'tab:orange')
ax3.plot(x,-y,'tab:green')
ax4.plot(x,-y**2,'tab:red')

for ax in fig.get_axes():
    ax.label_outer()
    
data={'apples':10,'oranges':15,'lemons':5,'limes':20}
names=list(data.keys())
values=list(data.values())

fig,axs=plt.subplots(1,3,figsize=(9,3),sharey=True)
axs[0].bar(names,values)
axs[1].scatter(names,values)
axs[2].plot(names,values)
fig.suptitle('Categorical Plotting')

data={'apples':10,'oranges':15,'lemons':5,'limes':20}
names=list(data.keys())
values=list(data.values())

fig,axs=plt.subplots(1,3,figsize=(9,3),sharex=True)
axs[0].bar(names,values)
axs[1].scatter(names,values)
axs[2].plot(names,values)
fig.suptitle('Categorical Plotting')

fig,axs=plt.subplots(ncols=3,nrows=3)
gs=axs[1,2].get_gridspec()

for ax in axs[1:,-1]:
    ax.remove()
axbig=fig.add_subplot(gs[1:,-1])
axbig.annotate('Big Axes',(0.1,0.5),xycoords='axes fraction',va='center')
fig.tight_layout()
plt.show()    



fig,axs=plt.subplots(ncols=3,nrows=3)
gs=axs[1,2].get_gridspec()

for ax in axs[1:,-1]:
    ax.remove()
axbig=fig.add_subplot(gs[2:,-2])
axbig.annotate('Big Axes',(0.1,0.5),xycoords='axes fraction',va='center')
fig.tight_layout()
plt.show()    

t=np.arange(0.01,10.0,0.01)
data1=np.exp(t)
data2=np.sin(2*np.pi*t)
fig.ax1=plt.subplots()
color='tab:red'
ax1.set_xlabel('time(s)')
ax1.set_ylabel('exp',color=color)
ax1.plot(t,data1,color=color)
ax1.tick_params(axis='y',labelcolor=color)
ax2=ax1.twinx()
color='tab:blue'
ax2.set_ylabel('sin',color=color,label='a')
ax2.plot(t,data2,color=color)
ax2.tick_params(axis='y',labelcolor=color)
fig.tight_layout()
plt.show()


import datetime
import pandas as pd
import pandas_datareader.data as web
start=datetime.datetime(2018,1,1)
end=datetime.datetime(2019,12,1)

tesla=web.DataReader('TSLA','yahoo',start,end)
fig=plt.figure()
ax1=plot.subplot2grid((1,1),(0,0))
ax1.plot_date(tesla.index,tesla['Close'],'-',label='Price')
ax1.plot([],[],linewidth=5,label='loss',color='r',aplha=0.5)
ax1.plot([],[],linewidth=5,label='gain',color='g',aplha=0.5)

ax1.fill_between(tesla,index,tesla['Close'],tesla['Close'][0],where=(tesla['Close']>tesla['Close'][0]),facecolor='g',alpha=0.5)
ax1.fill_between(tesla,index,tesla['Close'],tesla['Close'][0],where=(tesla['Close']<tesla['Close'][0]),facecolor='r',alpha=0.5)



wine=pd.read_csv('winequality.csv',delimiter=';')
data=[wine['alcohol'],wine['fixed acidity'],wine['quality']]
plt.violinplot(data,showmeans=True)
corr=wine.corr()
plt.figure(figsize=(12,9))
plt.imshow(corr, cmap='hot')
plt.colorbar()
plt.xticks(range(len(corr)),corr.columns,rotation=20)
plt.yticks(range(len(corr)),corr.columns)

conda install -c anaconda bs4
import bs4
import requests
url='https://finance.yahoo.com/currencies'
response=requests.get(url)
webpage=bs4.BeautifulSoup(response.text,'html.parser')
table=webpage.find("table")
rows=table.find_all("tr")
cy_data=[]

for row in rows:
    cells=row.find_all('td')
    cells=cells[1:3]
    cy_data.append([cell.text for cell in cells])

final=pd.DataFrame(cy_data).drop(0,axis=0)
final.columns=['currency','rate']
print(final)


import datetime as dt
import pickle
import bs4 as bs
import os

resp=requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
soup=bs4.BeautifulSoup(resp.text,'lxml')
table=soup.find('table',{'class':'wikitable sortable'})
tickers=[]
for row in table.findAll('tr')[1:]:
    ticker=row.findAll('td')[0].text.strip().replace('.','-')
    tickers.append(ticker)
if not os.path.exists('stock_dfs'):
    os.makedirs('stock_dfs')
start=dt.datetime(2019,1,1)
end=dt.datetime.now()
for ticker in tickers:
    if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
        df=web.DataReader(ticker,'yahoo',start=start,end=end)
        df.to_csv('stock_dfs/{}.csv'.format(ticker))
        print("Added {}".format(ticker))
    else:
        print("Already have {}".format(ticker))

main_df=pd.DataFrame()
for count,ticker in enumerate(tickers[0:51]):
    df=pd.read_csv('stock_dfs/{}.csv'.format(ticker))
    df.set_index('Date',inplace=True)
    df.rename(columns={'Adj Close':ticker},inplace=True)
    df.drop(['Open','High','Low','Close','Volume'],1,inplace=True)
    
    if main_df.empty:
        main_df=df
    else:
        main_df=main_df.join(df,how='outer')
    
    if(count%10==0):
        print(count)
print(main_df.head())

df=main_df.copy()
df_corr=df.corr()
print(df_corr.head())
import matplotlib.pyplot as plt
data1=df_corr.values
fig1=plt.figure()
ax1=fig1.add_subplot(111)

heatmap1=ax1.pcolor(data1,cmap=plt.cm.RdYlGn)
fig1.colorbar(heatmap1)
