#Problems on Pattern Printing

def DisplayPattern(iNo):
    for i in range(-iNo,0,1):
        print(i,end="\t")

    for i in range(0,iNo+1,1):
        print(i,end="\t")
        
    print()

def main():
    print("Enter the Number : ")
    iValue = int(input())

    DisplayPattern(iValue)
    
if __name__ == "__main__":
    main()
