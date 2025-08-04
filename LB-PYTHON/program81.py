#Problems on Pattern Printing
#row = 4 col = 4
#   *   *   *   *
#   *           *
#   *           *
#   *           *
#   *   *   *   *

def DisplayPattern(row,col):
    if(row != col):
        print("Invalid Input!!!")
        return
    
    for i in range(1,row+1):
        for j in range(1,col+1):  
            if(i==1 or i==row or j==1 or j==col): 
                print("*",end="\t")
            else:
                print(" ",end="\t")
        print()

def main():
    print("Enter the Number of rows : ")
    iRow = int(input())

    print("Enter the Number of Columns : ")
    iCol = int(input())

    DisplayPattern(iRow,iCol)
    
if __name__ == "__main__":
    main()
