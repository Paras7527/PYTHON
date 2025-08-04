#Problems on Number

def EvenOdd(iNo):
    if(iNo%2 == 0):
        return True
    else:
        return False

def main():
    print("Enter the Number :")
    iValue = int(input())

    iRet = EvenOdd(iValue)
    if(iRet == True):
        print(f"{iValue} is Even")
    else : 
        print(f"{iValue} is Odd")
    
if __name__ == "__main__":
    main()