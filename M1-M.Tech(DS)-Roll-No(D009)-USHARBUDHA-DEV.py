import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

acqu=pd.read_csv("acquisitions.csv")
comp=pd.read_excel("company.xlsx")

acqu.isnull().sum()
comp.isnull().sum()



###Q1)
#Q1)
acqu.groupby('AcquisitionMonth').count()['AcquisitionYear'].idxmax()
#AcquisitionMonth
#April        85
#August       74
#December     68
#February     58
#Feburary      6
#January      71
#July         86
#June         91
#March        78
#May          78
#November     56
#October      84
#September    75
#Ans=June

#Q2)
acqu.groupby('ParentCompany').count()['AcquisitionYear'].idxmax()
#Ans=ParentCompany
#Apple         95
#Facebook      67
#Google       215
#IBM          162
#Microsoft    210
#Twitter       53
#Yahoo        114
#GOOGLE IS THE ANSWER

#Q3)
comp.groupby('Business').plot()['AcquisitionID']

#Q4)
combi=acqu.merge(comp,how='inner',on='AcquisitionID')
combi.groupby('Country').count()['AcquisitionYear']
#Ans= 1. USA=632,2.CAN=47,3.UK=34

#Q5)
combi.groupby(['ParentCompany'])['Value (USD)','Company'].max()
#Ans=
#                Value (USD)                Company
#ParentCompany                                     
#Apple          3.000000e+09                init.ai
#Facebook       1.900000e+10                    tbh
#Google         1.250000e+10              spider.io
#IBM            5.000000e+09  iPhrase Systems, Inc.
#Microsoft      2.620000e+10      media-streams.com
#Twitter        4.790000e+08                ZipDial
#Yahoo          5.700000e+09                eGroups


#Q6)
combi.groupby('Country')['ParentCompany'].count()
#Ans= UK,CAN,ISR,FRA,GER,etc.

#Q7)
plt.bar(combi['AcquisitionYear'],combi['Value (USD)'])

#Q8)
ud=combi.groupby(['AcquisitionYear','ParentCompany']).agg({'AcquisitionID':[('op1','count')]})['AcquisitionID']['op1'].unstack()
x=ud.index
Apple=ud['Apple']
Fb=ud['Facebook']
gg=ud['Google']
Ibm=ud['IBM']
yahoo=ud['Yahoo']
msft=ud['Microsoft']
label=combi['ParentCompany'].unique()
fig,ax=plt.subplots()
ax.stackplot(x,Apple,Fb,gg,Ibm,yahoo,msft,labels=label)
plt.show()

#Q9)
x=combi.groupby('Country')['AcquisitionYear'].count().index
y=combi.groupby('Country')['AcquisitionYear'].count()
labels=x
sizes=y
#figsize=(60,40)
fig1,ax1=plt.subplots()
ax1.pie(sizes,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90,radius=1)
plt.show()



####Q3)
#Enter your numbers list
nos=[]
no_of_times=int(input("Enter the numbers you want to Add or Multiply:"))
for i in range(no_of_times+1):
    no=int(input("Enter a number "))
    nos.append(no)

num=nos
print("Enter your choice: Add or Multiply")
choice=input("\nEnter your choice:")

if choice=="Add":
    print(ad(num))
elif choice=="Multiply":
    print(mul(num))
else:
    print("Invalid Input")
    
   
def ad(num):
    summing=0
    for i in num:
        summing=summing+i
    return summing
def mul(num):
    mull=1
    for i in num:
        mull=mull*i
    return mull


####Q2)
from random import randint

probs = ['rock','paper','scissors']
opposites = {'rock':'paper','paper':'scissors','scissors':'rock'}
beats = {'rock':'scissors', 'paper':'rock', 'scissors':'paper'}

def controlProbs():
    if 'rock' not in probs:
        probs.append('rock')
    if 'scissors' not in probs:
        probs.append('scissors')
    if 'paper' not in probs:
        probs.append('paper')

def adjustProbs(choice):
    if len(probs)>20:
        probs.remove(choice)
        controlProbs()
    else:
        probs.append(beats[choice])

def pick():
    index=random.randint(0,len(probs)-1)
    return probs[index]

def controlInput(player):
    if len(player)!=1 or player not in 'rsp':
        return False
    return True

while True:
    player=input("Pick your element: ")
    if not controlInput:
        print("Please choose a valid one! i.e, (rock,paper,scissors)")
        continue
    computer = pick()
    print("My choice is: " + computer)
    if opposites[player] == computer:
        print("You Won!")
    elif opposites[computer] == player:
        print("You Lose!")
    else:
        print("Tie")











