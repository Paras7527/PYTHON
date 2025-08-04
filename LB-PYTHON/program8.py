def Addition(Value1,Value2):
    ans = 0
    ans = Value1 + Value2
    return ans

def main():
    print("Enter the First Number :")
    No1 = int(input())

    print("Enter the Second Number : ")
    No2 = int(input())

    iRet = Addition(No1,No2)
    print("Addition is : ",iRet)
    

if __name__ == "__main__":
    main()