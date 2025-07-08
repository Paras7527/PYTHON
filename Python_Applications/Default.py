def CalculatePercentage(Obtained,Total=600):
    Percentage = ((Obtained / Total) * 100)  #Business Logic
    return Percentage

def main():
    print("Enter Obtained Marks : ")
    Value1 = int(input())

    iRet = CalculatePercentage(Value1)   #Default Argument
    print("The Percentage is : ",iRet)
    
if __name__ == "__main__":
    main()