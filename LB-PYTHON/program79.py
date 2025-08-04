#Problems on Pattern Printing
#row = 4 col = 4
#   $   *   *   *
#   *   $   *   *
#   @   @   $   *
#   @   @   @   $

def DisplayPattern(row,col):
    if(row != col):
        print("Invalid Input!!!")
        return
    
    for i in range(0,row):
        for j in range(0,col):  
            if(i>j): 
                print("$",end="\t")
            elif(i==j):
                print("#",end="\t")
        print()

def main():
    print("Enter the Number of rows : ")
    iRow = int(input())

    print("Enter the Number of Columns : ")
    iCol = int(input())

    DisplayPattern(iRow,iCol)
    
if __name__ == "__main__":
    main()
