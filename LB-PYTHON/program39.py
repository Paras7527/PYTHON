#Problems on List / Array

def main():
    print("Enter the Number That you want :")
    iLength = int(input())

    Arr = []
    for i in range(1,iLength+1):
        no = int(input())
        Arr.append(no)

    print(Arr)


if __name__ == "__main__":
    main()