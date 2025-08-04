#Problems on Digits
def Display(iNo):
    i=1
    while(i<=iNo):
        print("*",end="\t")
        i = i + 1
    print("")

def main():
    print("Enter the number that you want ")
    ivalue = int(input())

    Display(ivalue)

if __name__ == "__main__":
    main()