import pandas as pd
import seaborn as sb

dataFrame = pd.read_csv("train.csv")

countNaN = 0
bsmtExposure = {}
dataImputationFlag = False

for i in range(len(dataFrame)):
    #if math.isnan(dataFrame["BsmtExposure"][i]):
    if not isinstance(dataFrame["BsmtExposure"][i],str):
        countNaN += 1
    else:
        if dataFrame["BsmtExposure"][i] in bsmtExposure:
            bsmtExposure[dataFrame["BsmtExposure"][i]] += 1
        else:
            bsmtExposure[dataFrame["BsmtExposure"][i]] = 1

'''
# Mode

mode = 0
modeVal = 0
for i in bsmtExposure:
    if bsmtExposure[i] > modeVal :
        modeVal = bsmtExposure[i]
        mode = i
dataFrameImputed = dataFrame["BsmtExposure"].fillna(mode)
dataImputationFlag = True
'''
'''
# New Category

dataFrameImputed = dataFrame["BsmtExposure"].fillna("Missing")
dataImputationFlag = True
'''

if dataImputationFlag :
    sb.countplot(dataFrameImputed)
else:    
    print("Missing data percentage in BsmtExposure is ", countNaN/len(dataFrame)*100,"%")
    sb.countplot(dataFrame["BsmtExposure"])