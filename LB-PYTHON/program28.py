#Problems on Digits

def CountOccurrence(iNo):
    iDigit = 0
    iCount = 0
    while(iNo!=0):
        iDigit = iNo%10
        if(iDigit == 5):
            iCount = iCount + 1
        iNo = iNo//10
    return iCount

def main():
    print("Enter the number : ")
    ivalue = int(input())

    iRet = CountOccurrence(ivalue)
    print("The frequency of 5 is : ",iRet)

if __name__ == "__main__":
    main()