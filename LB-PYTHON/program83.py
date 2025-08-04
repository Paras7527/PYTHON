#Problems on Pattern Printing
#row = 5 col = 4
#   *   *   *   *
#   *   *   *   *
#   *   *   *   *
#   *   *   *   *
#   *   *   *   *

def DisplayPattern(row,col):
    for i in range(1,row+1):
        print("$\t"*col)

def main():
    print("Enter the Number of rows : ")
    iRow = int(input())

    print("Enter the Number of Columns : ")
    iCol = int(input())

    DisplayPattern(iRow,iCol)
    
if __name__ == "__main__":
    main()
