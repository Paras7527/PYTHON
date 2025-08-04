#Problems on Digits
def SumDigits(iNo):
    iDigit = 0
    iSum = 0
    while(iNo!=0):
        iDigit = iNo%10
        iSum = iSum + iDigit
        iNo = iNo//10
    return iSum
def main():
    print("Enter the number that you want ")
    ivalue = int(input())

    iRet = SumDigits(ivalue)
    print("Sum of Digit is : ",iRet)

if __name__ == "__main__":
    main()