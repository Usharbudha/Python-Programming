import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

hotel=pd.read_csv('hotel_bookings.csv')

hotel.isnull().sum()

#Removed company because it had 112593 missing values.
hotel=hotel.drop(['company'],axis=1)
hotel=hotel.dropna(axis=0)

#highest guests from a country
fig = plt.figure(figsize=(20,10))
plt.pie(hotel['country'].value_counts(),labels=hotel['country'].value_counts().index)
fig.set_facecolor('lightgrey')
plt.show()

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
hotel['hotel']=le.fit_transform(hotel['hotel'])
hotel['arrival_date_month']=hotel['arrival_date_month'].map({'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12})
hotel['arrival_date_month']=le.fit_transform(hotel['arrival_date_month'])
hotel['meal']=le.fit_transform(hotel['meal'])
hotel['country']=le.fit_transform(hotel['country'])
hotel['market_segment']=le.fit_transform(hotel['market_segment'])
hotel['distribution_channel']=le.fit_transform(hotel['distribution_channel'])
hotel['reserved_room_type']=le.fit_transform(hotel['reserved_room_type'])
hotel['assigned_room_type']=le.fit_transform(hotel['assigned_room_type'])
hotel['deposit_type']=le.fit_transform(hotel['deposit_type'])
hotel['customer_type']=le.fit_transform(hotel['customer_type'])
hotel['reservation_status']=le.fit_transform(hotel['reservation_status'])
hotel['reservation_status_date']=le.fit_transform(hotel['reservation_status_date'])

#REMOVING NULL VALUES
hotel['country'].value_counts()
hotel['country'].fillna(hotel['country'].mean())

hotel['children'].fillna(hotel['children'].mean())

#Since there were too many na's (less in comparision of the company column) in this column, so I've replaced na with zero instead of dropping the column
hotel['agent'].fillna(0)



#VISUALIZATION
import seaborn as sns
sns.heatmap(hotel.corr())

sns.countplot(x='hotel',data=hotel)
sns.countplot(x='reservation_status',data=hotel)
#we can see the relationship between people who stayed on weekdays and weekends below
# 0= check-out, 1=canceled, 2=no-show
sns.boxplot(x='reservation_status',y='stays_in_weekend_nights',data=hotel)
sns.boxplot(x='reservation_status',y='stays_in_week_nights',data=hotel)

#from below we can see relation between month and reservation status
# 0= Jan, 1= Feb,... and so on till 11=dec
sns.countplot(x='arrival_date_month',data=hotel,hue='reservation_status')

#below we can see relation between reservation status and guest
sns.countplot(x='adults',data=hotel,hue='reservation_status')

sns.countplot(x='children',data=hotel,hue='reservation_status')

sns.countplot(x='babies',data=hotel,hue='reservation_status')

#now lets see relation between, cancelation and deposit
#here 0=no deposit, 1= non-refund, 2=refundable deposit type
sns.countplot(x='deposit_type',data=hotel,hue='is_canceled')

#linear regression model 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression

X=hotel.drop(['previous_cancellations'],axis = 1)
Y=hotel['previous_cancellations']

X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=0)
lir=LinearRegression()  
lir.fit(X_train, y_train) 
y_pred=lir.predict(X_test)

print('MSE:',metrics.mean_squared_error(y_test, y_pred))
