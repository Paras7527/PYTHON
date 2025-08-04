#Problems on Number

def ChkMax(iNo1,iNo2,iNo3):
    if(iNo1>iNo2 and iNo1>iNo3):
        return iNo1
    elif(iNo2>iNo3 and iNo2>iNo1):
        return iNo2
    else:
        return iNo3
       

def main():
    print("Enter the First Number :")
    iValue1 = int(input())

    print("Enter the Second Number :")
    iValue2 = int(input())

    print("Enter the Third Number :")
    iValue3 = int(input())

    iRet = ChkMax(iValue1,iValue2,iValue3)
    print("Max value is : ",iRet)


    
if __name__ == "__main__":
    main()