from functools import reduce

def CheckEven(No):
    return No % 2 == 0

def Increase(No):
    return No + 1

def Sum(A,B):
    return A + B

Data = [7,10,15,12,4,6,9,8,12,16]
print("Input Data : ", Data)

FData=list(filter(CheckEven,Data))
print("Filter Data : ", FData)

MData=list(map(Increase,FData))
print("Map Data : ",MData)

RData=reduce(Sum,MData)
print("Reduce Data :",RData)