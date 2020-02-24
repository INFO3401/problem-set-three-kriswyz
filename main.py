import pandas as pd
import matplotlib.pyplot as plt
from utils import *

def loadAndCleanData(filename):
	data = pd.read_csv(filename)
	df = data.fillna(0)
	print(data)
	return data

df = loadAndCleanData("creditData.csv")

print("The probability is : ")
print(computeProbability("age",[0,40],df))
#print(computePDF("MonthlyIncome",df))
print(viewDistribution(row,df))
print("The conditional probability is : ")
print(computeDefaultRisk("SeriousDlqin2yrs",[bin.left,bin.right],row,df))


def loadAndCleanData2(filename):
	Data2  = pd.read_csv(filename)
	df = Data2.fillna(0)
	print(Data2)
	return Data2

data2 = loadAndCleanData2("newLoans.csv")


print("The conditional probability is : ")
print(predictDefaultRisk(row, data2))
print(computePDF("SeriousDlqin2yrs",data2))


