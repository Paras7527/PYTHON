#Problems on Digits

def SumFactor(iNo):
    iSum = 0
    for i in range(1,(iNo//2)+1):
        if(iNo%i==0):
            iSum = iSum + i
    return iSum
def main():
    print("Enter the number : ")
    ivalue = int(input())

    iRet = SumFactor(ivalue)
    print("Summation of factors : ",iRet)

    
if __name__ == "__main__":
    main()