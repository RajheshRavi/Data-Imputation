import pandas as pd
import math
import matplotlib.pyplot as plt
import random
import statistics

dataFrame = pd.read_csv('train.csv')
#print(dataFrame["Age"])
ageList = []
survive = []
dataImputedFlg = False

for i in range(len(dataFrame["Age"])):
    if not math.isnan(dataFrame["Age"][i]):
        ageList.append(dataFrame["Age"][i])
        survive.append(dataFrame["Survived"][i])

x = []
y = []

for i in range(int(max(ageList))+1):
    x.append(int(i))
    y.append(0)
for i in ageList:
    y[int(i)]+=1


'''
# Mean

dataImputedFlg = True
mean = sum(ageList)/len(ageList)
print("Mean before imputation",mean)
for i in range(0,len(dataFrame["Age"]) - len(ageList)):
    y[int(mean)]+=1
    ageList.append(mean)
imputedData = dataFrame['Age'].fillna(mean)
'''
'''
# Median

dataImputedFlg = True
ageList.sort()
median = ageList[len(ageList)//2]
print("Median before imputation",median)
for i in range(0,len(dataFrame["Age"]) - len(ageList)):
    y[int(median)]+=1
    ageList.append(median)
imputedData = dataFrame['Age'].fillna(median)
'''
'''
# End of Tail 

dataImputedFlg = True
maxValue = max(ageList)
print("Tail Value",maxValue)
for i in range(0,len(dataFrame["Age"]) - len(ageList)):
    y[int(maxValue)]+=1
    ageList.append(maxValue)
imputedData = dataFrame['Age'].fillna(maxValue)
'''
'''
# Random

dataImputedFlg = True
randValue = random.choice(ageList)
print("Random value for imputation",randValue)
for i in range(0,len(dataFrame["Age"]) - len(ageList)):
    y[int(randValue)]+=1 
    ageList.append(randValue)
imputedData = dataFrame['Age'].fillna(randValue)
'''

if not dataImputedFlg:
    print("Percentage of Missing values is",str(100-(len(ageList)*100/len(dataFrame["Age"])))+" %")

plt.scatter(x,y)
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

print("Mean is", statistics.mean(ageList))
print("Variance is ",statistics.variance(ageList))

print("Covariance :")
if dataImputedFlg :
    print(pd.DataFrame({"Age":imputedData,"Survived":dataFrame["Survived"]}).cov())
else:
    print(pd.DataFrame({"Age":ageList,"Survived":survive}).cov())