#Problems on List / Array
def Update(Brr):
    i=0
    for i in range(len(Brr)-1,-1,-1):
        if(Brr[i] % 2 ==0):
            Brr[i] = Brr[i] + 1
def main():
    print("Enter the Number That you want :")
    iLength = int(input())

    Arr = []
    for i in range(1,iLength+1):
        no = int(input())
        Arr.append(no)

    Update(Arr)

    print(Arr)

if __name__ == "__main__":
    main()

#Call By reference is There in python!!!!