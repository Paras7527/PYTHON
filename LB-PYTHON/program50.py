#Problems on List / Array
def ReverseArray(Brr):
    iStart = 0
    iEnd = len(Brr)-1
    
    while(iStart < iEnd):
        Brr[iStart],Brr[iEnd] = Brr[iEnd],Brr[iStart]
        iStart = iStart + 1
        iEnd = iEnd - 1

def main():
    print("Enter the Number That you want :")
    iLength = int(input())

    Arr = []
    for i in range(1,iLength+1):
        no = int(input())
        Arr.append(no)

    ReverseArray(Arr)

    print(Arr)

if __name__ == "__main__":
    main()
