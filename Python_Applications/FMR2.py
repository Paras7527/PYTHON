#Normal function to Lambda Function
from functools import reduce

CheckEven=lambda No : No % 2 == 0

Increase=lambda No : No+1

Sum=lambda A , B : A + B

Data = [7,10,15,12,4,6,9,8,12,16]
print("Input Data : ", Data)

FData=list(filter(CheckEven,Data))
print("Filter Data : ", FData)

MData=list(map(Increase,FData))
print("Map Data : ",MData)

RData=reduce(Sum,MData)
print("Reduce Data :",RData)