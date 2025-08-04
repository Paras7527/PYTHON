#Problems on Digits
def Display(iNo):
    iSum = 0
    for i in range(1,iNo+1):
        iSum = iSum + i
    return iSum
def main():
    print("Enter the number that you want ")
    ivalue = int(input())

    iRet = Display(ivalue)
    print("Addition is : ",iRet)

if __name__ == "__main__":
    main()