import sys

def main():
    print("Number of Command line argumnets are : ",len(sys.argv))
    print("Data Type of argv is : ",type(sys.argv))
    for i in range(len(sys.argv)):      #Type 1
        print(sys.argv[i])

    for value in sys.argv:              #Type 2
        print(value)

if __name__ == "__main__":
    main()
