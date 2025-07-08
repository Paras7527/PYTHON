CheckEven=lambda No : No % 2 == 0
Increase=lambda No : No+1
Sum=lambda A , B : A + B

def filterX(Task,Values):
    Result=[]
    for no in Values:
        #Result.append(Task(no))
        ret=Task(no)
        if(ret==True):
            Result.append(no)  

    return Result

def mapX(Task,Values):
    Result=[]
    for no in Values:
        ret=Task(no)
        Result.append(ret)

    return Result

def reduceX(Task,Values):
    #[11, 13, 5, 7, 9, 13, 17]
    Result=0
    for no in Values:
        Result=Task(Result,no)

    return Result


Data = [7,10,15,12,4,6,9,8,12,16]
print("Input Data : ", Data)

FData=list(filterX(CheckEven,Data))
print("Filter Data : ", FData)

MData=list(mapX(Increase,FData))
print("Map Data : ",MData)

RData=reduceX(Sum,MData)
print("Reduce Data :",RData)