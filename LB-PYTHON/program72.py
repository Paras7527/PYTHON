#Problems on Pattern Printing

def DisplayPattern(iNo):
    for i in range(-iNo,iNo+1,1):
        print(i,end="\t")

    print()

def main():
    print("Enter the Number : ")
    iValue = int(input())

    DisplayPattern(iValue)
    
if __name__ == "__main__":
    main()
