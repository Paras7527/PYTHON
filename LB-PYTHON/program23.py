#Problems on Digits
def Factorial(iNo):
    ifact = 1
    for i in range(1,iNo+1):
        ifact = ifact * i
    return ifact
def main():
    print("Enter the number that you want ")
    ivalue = int(input())

    iRet = Factorial(ivalue)
    print("Factorial of number is : ",iRet)

if __name__ == "__main__":
    main()