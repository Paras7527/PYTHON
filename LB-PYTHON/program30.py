#Problems on Digits

def DisplayFactor(iNo):
    print(f"Factor of {iNo} are : ")
    for i in range(1,iNo):
        if(iNo%i==0):
            print(i,end="\t")
def main():
    print("Enter the number : ")
    ivalue = int(input())

    DisplayFactor(ivalue)

    
if __name__ == "__main__":
    main()