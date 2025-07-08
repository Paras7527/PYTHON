def main():
    Ans=0
    try:
        print("Enter First Number : ")
        iValue1=int(input())

        print("Enter Second Number : ")
        iValue2=int(input())

        Ans=iValue1/iValue2

    except ZeroDivisionError as zobj:
        print("Exception Occured Due to Second Input!",zobj)

    except ValueError as vobj:
        print("Invalid data type of input : ",vobj)
    print("Division is : ",Ans)

if __name__=="__main__":
    main()