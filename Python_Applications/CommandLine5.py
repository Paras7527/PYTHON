import sys

def main():
    print("Number of Command line argumnets are : ",len(sys.argv))
    print("Data Type of argv is : ",type(sys.argv))
    
    for i in range(1,len(sys.argv),1):      #Type 1
        print(sys.argv[i])


if __name__ == "__main__":
    main()
