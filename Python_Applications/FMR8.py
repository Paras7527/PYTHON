from MarvellousFMR import filterX,mapX,reduceX

CheckEven=lambda No : No % 2 == 0
Increase=lambda No : No+1
Sum=lambda A , B : A + B

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
