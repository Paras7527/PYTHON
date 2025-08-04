#Problems on Digits

def CountOccurrence(iNo):
    iDigit = 0
    iCount4 = 0
    iCount5 = 0
    iCount7 = 0
    while(iNo!=0):
        iDigit = iNo%10
        if(iDigit == 4 ):
            iCount4 = iCount4 + 1
        elif(iDigit == 5 ):
            iCount5= iCount5 + 1
        elif(iDigit == 7 ):
            iCount7 = iCount7 + 1
        iNo = iNo//10
    return iCount4,iCount5,iCount7

def main():
    print("Enter the number : ")
    ivalue = int(input())

    #iRet = CountOccurrence(ivalue)     The frequency of 4 , 5 and 7 is :  (4, 4, 3)
    iRet4,iRet5,iRet7 = CountOccurrence(ivalue)
    print(f"Frequency of 4 is :{iRet4} , Frequency of 5 is :{iRet5} , Frequency of 7 is :{iRet7}")


if __name__ == "__main__":
    main()