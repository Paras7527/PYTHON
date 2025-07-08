#Normal code [Not a lambda function]
def ChkEven(iNo):
    if((iNo%2)==0):
        return True
    else:
        return False
    
def main():
    print("Enter the Number : ")
    iValue=int(input())

    iRet=ChkEven(iValue)
    if(iRet==True):
        print("Number is Even")
    else:
        print("Number is Odd")

if __name__=="__main__":
    main()