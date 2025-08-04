#Problems on Number

def ChkDivisible(iNo):
    if(iNo%3 == 0 and iNo%5 == 0):
        return True
    else:
        return False

def main():
    print("Enter the Number :")
    iValue = int(input())

    iRet = ChkDivisible(iValue)
    if(iRet == True):
        print(f"{iValue} is Divisible by 3 & 5")
    else : 
        print(f"{iValue} is Not Divisible by 3 &(or) 5")
    
if __name__ == "__main__":
    main()