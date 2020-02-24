import pandas as pd
import csv
import matplotlib.pyplot as plt
#Co-work with Katlheen, Jihong, Sofia and Ziyang

#1:
#I think this xls file is computing the conditional probability of delinquency for potential clients, differentiating between percents and integers to compute scores/ratings.
#Terminal Code:
#cd folder name
#python file name


#2：
def loadAndCleanData(filename):
	data = pd.read_csv(filename)
	data.fillna(value = 0, inplace = True)
	print(data)
	return data
#3:
df = loadAndCleanData("creditData.csv")

#4:
#def computePDF(feature, data):
	#compute = data[feature].plot.kde()
	#plt.show(compute)



#5:
def viewDistribution(myCol, data):
	newPlot = data.hist(column = myCol)
	plt.show(newPlot)

#6:
def viewDistribution(myCol, data):
	newPlot = data.hist(column = myCol)
	dist = data.hist(log=True)
	plt.show(newPlot)
for feature in df.columns.values:
	viewLogDistribution(feature,df)

#7:
def equalBin(myCol, data)
	myBins = pd.qcut(data[myCol], q=3, duplicates='drop', retbins=False).unique()
	return myBins
for feature in df.columns.values:
	if feature != 'SeriousDlqin2yrs':
		equalBins(feature,df)

#8:
def computeProbability(feature, bin, data):
	#calculate the total number of data points
	#devide of the number people in the bin by total # of data points
	count = 0.0
	for i, dataPoint in data.iterrows():
		#see if the data in the right bin
		if dataPoint[feature] >= bin[0] and dataPoint[feature] < bin[1]:
			count += 1

	totalData = len(data)

	probability = count / totalData
	return probability


def computeDefaultRisk(myCol,feature,bin,data):
    count=0.0
    count2=0.0
    for i,dataPoint in data.iterrows():
        if dataPoint[feature]>=bin[0] and dataPoint[feature]<bin[1]:
            count+=1
            if dataPoint[myCol]==1:
                count2+=1
    totalData=len(data)
    probability=count/totalData
    probability2=count2/totalData
    conditionalProbability = probability2/probability
    print(conditionalProbability)

    return conditionalProbability

#9:

def loadAndCleanData2(filename):
	Data2  = pd.read_csv(filename)
	print(Data2)
	return Data2
risks = {}
for feature in df.columns.values:
	if feature != 'SeriousDlqin2yrs':
		featDict = {}
		featDict['left'] = (computeDefaultRisk('SeriousDlqin2yrs','left',feature,myDataframe))
		featDict['middle'] = (computeDefaultRisk('SeriousDlqin2yrs','middle',feature,myDataframe))
		featDict['right'] =(computeDefaultRisk('SeriousDlqin2yrs','right',feature,myDataframe))
		risks[feature] = featDict

#10:
data2 = loadAndCleanData2("newLoans.csv")

#11:
weights = {'age':0.025,'NumberOfDependents':0.025,'MonthlyIncome':0.1,'DebtRatio':0.1,'RevolvingUtilizationOfUnsecuredLines':0.1,'NumberOfOpenCreditLinesAndLoans':0.1,'NumberRealEstateLoansOrLines':0.1,'NumberOfTime30-59DaysPastDueNotWorse':0.15,'NumberOfTime60-89DaysPastDueNotWorse':0.15,'NumberOfTimes90DaysLate':0.15}

binSize = {}
def predictDefaultRisk(myRow,defaults,weights):
	probTable = []
	for feature in df.columns:
		if feature != 'SeriousDlqin2yrs':
			sideSize = {}
			try:
				sideSize['right'] = equalBins(feature,df)[0]
			except:
				sideSize['right'] = None
			try:
				sideSize['middle'] = equalBins(feature,df)[1]
			except:
				sideSize['middle'] = None
			try:
				sideSize['left'] = equalBins(feature,df)[2]
			except:
				sideSize['left'] = None
			binSize[feature] = sideSize


def predictDefaultRisk(myCol,feature,bin,data):
	count=0.0
    count2=0.0
    for i,dataPoint in data.iterrows():
        if dataPoint[feature]>=bin[0] and dataPoint[feature]<bin[1]:
            count+=1
            if dataPoint[myCol]==1:
                count2+=1
    totalData=len(data)
    probability=count/totalData
    probability2=count2/totalData
    conditionalProbability = probability2/probability
    print(conditionalProbability)

    return conditionalProbability

#12:
	val = predictDefaultRisk(data2.iloc[[row]],risks,weights)
	data2['SeriousDlqin2yrs'][row] = val
#13:
computePDF('SeriousDlqin2yrs',df)
#It will turns to 0 in the end.
