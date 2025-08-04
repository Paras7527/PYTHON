#Problems on Digits
def DisplayDigits(iNo):
    iDigit = 0
    while(iNo!=0):
        iDigit = iNo%10
        iNo = iNo//10
        print(iDigit)
def main():
    print("Enter the number that you want ")
    ivalue = int(input())

    iRet = DisplayDigits(ivalue)
    print("digits are : ",iRet)

if __name__ == "__main__":
    main()