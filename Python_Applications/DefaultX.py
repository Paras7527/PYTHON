def CalculatePercentage(Obtained=418,Total=600):
    Percentage = ((Obtained / Total) * 100)  #Business Logic
    return Percentage

def main():

    iRet = CalculatePercentage(350,450)   #Default Argument
    print("The Percentage is : ",iRet)
    
    iRet = CalculatePercentage(350)   #Default Argument
    print("The Percentage is : ",iRet)
    
    iRet = CalculatePercentage()   #Default Argument
    print("The Percentage is : ",iRet)
if __name__ == "__main__":
    main()