#Problems on Digits
def Display(iNo):
    for i in range(1,iNo+1):
        print("*",end="\t")
    print("")

def main():
    print("Enter the number that you want ")
    ivalue = int(input())

    Display(ivalue)

if __name__ == "__main__":
    main()