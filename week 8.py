import numpy as np
import pandas as pd
import datetime
import pandas_datareader.data as web
iris=pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
import seaborn as sns

iris['sepal_length'].mean() #5.8843

iris['Avg_Sepal_Length']=np.where(iris['sepal_length']>5.84,'Above Avg','Below Avg')

iris_new={'setosa':'Se','versicolor':'Ve','virginica':'Vi'}

iris['species']=iris['species'].map(iris_new)
iris['species']=iris['species'].astype('category')

import matplotlib.pyplot as plt
import datetime


plt.plot([1.5,3.0])
plt.show()

plt.plot([5,3.0])
plt.title('Interactive Plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()

a=[1,2,6,7]
b=[1,2,3,4]

plt.plot(b,a)
plt.show()

start=datetime.datetime(2012,1,1)
end=datetime.datetime(2020,1,1)

stock=web.DataReader('GOOG','yahoo',start,end)
ts=stock['Close']
plt.plot(ts)
plt.xticks(rotation=20)
plt.show()

import calendar
calendar.month_name[1:13]
month_num=[1,2,3,4,5,6,7,8,9,10,11,12]

units_sold=[500,600,750,900,1100,1050,1000,950,800,700,550,450]
fig, ax=plt.subplots()
plt.xticks(month_num,calendar.month_name[1:13],rotation=20)
plot=ax.bar(month_num,units_sold)
plot[0].get_height()

for rect in plot:
    height=rect.get_height()
    ax.text(rect.get_x()+rect.get_width()/2.,1.002*height,'%d' %int(height),ha='center',va='bottom')

plt.show()


month_num=[1,2,3,4,5,6,7,8,9,10,11,12]

units_sold=[500,600,750,900,1100,1050,1000,950,800,700,550,450]
fig, ax=plt.subplots()
plt.xticks(month_num,calendar.month_name[1:13],rotation=20)
plot=ax.barh(month_num,units_sold)
plot[0].get_height()

for rect in plot:
    height=rect.get_height()
    ax.text(rect.get_x()+rect.get_width()/2.,1.002*height,'%d' %int(height),ha='center',va='bottom')

plt.scatter(month_num,units_sold)
plt.show()



iris=pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
iris['species']=iris['species'].map({'setosa':0,'versicolor':1,'virginica':2})
plt.scatter(iris.petal_length,iris.petal_width,s=50*iris.petal_length*iris.petal_width,c=iris.species,alpha=0.3)
plt.show()

x=np.array([1,2,3,4,5,6],dtype=np.int32)
apr=[5,7,5,8,7,9]
may=[0,4,3,7,8,9]
june=[6,7,4,5,6,8]

labels=['April','May','June']

fig, ax=plt.subplots()
ax.stackplot(x,apr,may,june,labels=labels)
ax.legend(loc=2)

plt.xlabel('defect reason code')
plt.ylabel('no. of defect')
plt.title('Predict Defects-Q1 FY2019')
plt.show()


grp_exp=np.array([12,13,14,15,16,17,17,18,10,1,2,3,4,5,6,7,8,9,0,2,3,5,6,7,9,0,2,31,45,67,89,45,67,])
nbins=21
n,bins,patches=plt.hist(grp_exp,bins=nbins)

plt.xlabel('EX of years')
plt.ylabel('Frequency')
plt.title('Distribution of EX')
plt.axvline(x=grp_exp.mean(),linewidth=2,color='r')
plt.show()

np.random(0,100,60) #to create random number




labels=['Sci-Fi','Drama','Thriller','Nolan Bhaisahab']
sizes=[5,15,20,60]
explode=(0,0,0,0.1)
color_list=['red','yellow','green','blue']
fig1, ax1=plt.subplots()
ax1.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
plt.show()

fig1, ax1=plt.subplots()
ax1.pie(sizes,explode=explode,labels=labels,autopct='%1%%',shadow=True,startangle=90,colour=color_list)


###

rows = ['2011','2012','2013','2014','2015']
columns = ('7Ah','35Ah','40Ah','135Ah','150Ah')

data = [[75,144,114,109,108],
        [90,126,102,84,116],
        [96,114,75,105,135],
        [105,90,150,90,75],
        [90,140,56,85,97]]

values = np.arange(0,600,100)

colors = plt.cm.OrRd(np.linspace(0,0.5,len(rows)))
n_rows = len(data)
index = np.arange(len(columns)) + 0.3
bar_width = 0.9

y_offset = np.zeros(len(columns))
fig, ax = plt.subplots()

cell_text = []

for row in range(n_rows):
    plot = plt.bar(index, data[row], bar_width, bottom = y_offset, color = colors[row])
    y_offset = y_offset + data[row]
    cell_text.append(['%1.1f'%(x) for x in y_offset])
    i=0
    for rect in plot:
        ax.text(rect.get_x() + rect.get_width()/2, y_offset[i], '%d' % int(y_offset[i]), ha = 'center', va = 'bottom')
        i = i+1
       
the_table = plt.table(cellText = cell_text, rowLabels = rows, colLabels = columns, loc = 'bottom')

plt.ylabel('Units Sold')
plt.title('Number of Batteries Sold/Year')
plt.xticks([])
plt.show()

#Polar chart
Depts=["COGS",'IT','Payroll','R & D','Sales & Marketing']

ra=[30,15,25,10,20,30]
rp=[32,20,23,11,14,32]

plt.figure(figsize=(10,6))
plt.subplot(polar=True)

theta=np.linspace(0,2*np.pi,len(rp))
(lines,labels)=plt.thetagrids(range(0,360,int(360/len(Depts))),(Depts))

plt.plot(theta,rp)
plt.fill(theta,rp,'b',alpha=0.4)
plt.plot(theta,ra)
plt.legend(labels=('Plan','Actual'),loc=1)
plt.title("Plan vs Actual spend by department")
plt.show()


wine=pd.read_csv('winequality.csv',delimiter=';')
data=[wine['alcohol'],wine['fixed acidity'],wine['quality']]
plt.boxplot(data)
plt.boxplot(data,vert=False,flierprops=dict(markerfacecolor='r',marker='D'))
plt.show()

wine=pd.read_csv('winequality.csv',delimiter=';')
data=[wine['alcohol'],wine['fixed acidity'],wine['quality']]
plt.violinplot(data,showmeans=True)



























