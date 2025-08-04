#Problems on Pattern Printing
#row = 4 col = 4
#   $   *   *   *
#   *   $   *   *
#   *   *   $   *
#   *   *   *   $

def DisplayPattern(row,col):
    #Filter
    if(row != col):
        print("Invalid Input!!!")
        return
    
        #Nested Loop
    for i in range(0,row):          #For Rows
        for j in range(0,col):  
            if(i==j):    #For Colums
                print("$",end="\t")
            else:
                print("*",end="\t")
        print()

def main():
    print("Enter the Number of rows : ")
    iRow = int(input())

    print("Enter the Number of Columns : ")
    iCol = int(input())

    DisplayPattern(iRow,iCol)
    
if __name__ == "__main__":
    main()
