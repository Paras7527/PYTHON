def CalculatePercentage(Total,Obtained):
    Percentage = ((Obtained / Total) * 100)  #Business Logic
    return Percentage

def main():
    print("Enter Total Marks : ")
    Value1 = int(input())
    
    print("Enter Obtained Marks : ")
    Value2 = int(input())

    iRet = CalculatePercentage(Total=Value1,Obtained=Value2)   #KeyWord Argument
    print("The Percentage is : ",iRet)
    
if __name__ == "__main__":
    main()