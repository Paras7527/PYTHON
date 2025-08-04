#Problems on List / Array
def MinArray(Brr):
    iMin = 0
    for no in Brr:
        if(no < iMin):
            iMin = no
    return iMin

def main():
    print("Enter the Number That you want :")
    iLength = int(input())

    Arr = []
    for i in range(1,iLength+1):
        no = int(input())
        Arr.append(no)

    iRet = MinArray(Arr)
    print("The Min Element in the list is :",iRet)

if __name__ == "__main__":
    main()