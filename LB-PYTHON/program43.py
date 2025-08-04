#Problems on List / Array
def CountEvenOdd(Brr):
    iCountEven = 0
    iCountOdd = 0

    for no in Brr:
        if(no % 2 == 0):
            iCountEven = iCountEven + 1
        else:
            iCountOdd = iCountOdd + 1

    return iCountOdd,iCountEven

def main():
    print("Enter the Number That you want :")
    iLength = int(input())

    Arr = []
    for i in range(1,iLength+1):
        no = int(input())
        Arr.append(no)

    iRet1,iRet2 = CountEvenOdd(Arr)
    print("The Number of odd elements are :",iRet1)
    print("The Number of even elements are : ",iRet2)

if __name__ == "__main__":
    main()