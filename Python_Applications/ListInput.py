def main():
    print("Enter Number of Elements : ")
    size=int(input())

    Data=list()

    print("Enter the Values : ")

    for i in range(size):
        no=int(input())
        Data.append(no)

    print("Entered Elements are:")
    for value in Data:
        print(value)

if __name__ == "__main__":
    main()