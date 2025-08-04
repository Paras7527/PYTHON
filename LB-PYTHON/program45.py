#Problems on List / Array
def ReverseList(Brr):
    i=0
    for i in range(len(Brr)-1,-1,-1):
        print(Brr[i])



def main():
    print("Enter the Number That you want :")
    iLength = int(input())

    Arr = []
    for i in range(1,iLength+1):
        no = int(input())
        Arr.append(no)

    ReverseList(Arr)

if __name__ == "__main__":
    main()