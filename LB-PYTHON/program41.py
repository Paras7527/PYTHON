#Problems on List / Array
def MaxArray(Brr):
    iMax = 0
    for no in Brr:
        if(no > iMax):
            iMax = no
    return iMax

def main():
    print("Enter the Number That you want :")
    iLength = int(input())

    Arr = []
    for i in range(1,iLength+1):
        no = int(input())
        Arr.append(no)

    iRet = MaxArray(Arr)
    print("The Max Element in the list is :",iRet)

if __name__ == "__main__":
    main()