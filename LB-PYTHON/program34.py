#Problems on Digits

def ChkPerfect(iNo):
    iSum = 0
    for i in range(1,(iNo//2)+1):
        if(iNo%i==0):
            iSum = iSum + i

    return (iSum == iNo)

    
def main():
    print("Enter the number : ")
    ivalue = int(input())

    iRet = ChkPerfect(ivalue)
    if(iRet):
        print("The Number is a Perfect Number ")
    else:
        print("The Number is not a Perfect number")

if __name__ == "__main__":
    main()