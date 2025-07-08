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

def main():
    Data =[]
    print("Enter the Number : ")
    Size=int(input())
    
    print("Please Enter Numberic Value : ")
    for i in range(Size):
        no=int(input())
        Data.append(no)

    print("Input Data : ", Data)

    FData=list(filterX(CheckEven,Data))
    print("Filter Data : ", FData)

    MData=list(mapX(Increase,FData))
    print("Map Data : ",MData)

    RData=reduceX(Sum,MData)
    print("Reduce Data :",RData)

if __name__ == "__main__":
    main()
