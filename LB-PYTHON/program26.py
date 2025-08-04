#Problems on Digits
def CountEven(iNo):
    iDigit = 0
    iCount = 0
    while(iNo!=0):
        iDigit = iNo%10
        if(iDigit % 2 == 0):
            iCount = iCount + 1
        iNo = iNo//10
    return iCount
def main():
    print("Enter the number : ")
    ivalue = int(input())

    iRet = CountEven(ivalue)
    print("Even Digits are : ",iRet)

if __name__ == "__main__":
    main()