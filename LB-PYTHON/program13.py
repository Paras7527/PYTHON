#Problems on Number

def Division(iNo1,iNo2):
    Ans = 0
    Ans = iNo1 // iNo2  #Floor Division
    return Ans

def main():
    print("Enter the First Number :")
    iValue1 = int(input())

    print("Enter the Second Number :")
    iValue2 = int(input())

    iRet = Division(iValue1,iValue2)
    print("Division is : ",iRet)

if __name__ == "__main__":
    main()