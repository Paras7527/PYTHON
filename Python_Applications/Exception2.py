def main():
    print("Enter First Number : ")
    iValue1=int(input())

    print("Enter Second Number : ")
    iValue2=int(input())

    Ans=0
    try:
        Ans=iValue1/iValue2
    except ZeroDivisionError:
        print("Exception Occured Due to Second Input! ")

    print("Division is : ",Ans)

if __name__=="__main__":
    main()