#Problems on List / Array
def SumArray(Brr):
    iSum = 0
    for no in Brr:
        iSum = iSum + no
    return iSum

def main():
    print("Enter the Number That you want :")
    iLength = int(input())

    Arr = []
    for i in range(1,iLength+1):
        no = int(input())
        Arr.append(no)

    iRet = SumArray(Arr)
    print("The Addition of Elements of the array :",iRet)

if __name__ == "__main__":
    main()