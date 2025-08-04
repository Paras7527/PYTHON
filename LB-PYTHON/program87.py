#Problems on Pattern Printing
#row = 5 
#      _* * * *_
#      __* * *__
#      ___* *___
#      ____*____

def DisplayPattern(row):
    for i in range(1,row+1):
        print(" "*(row-i),end="")
        print("* "*i)

    for i in range(row,0,-1):
        print(" "*(row-i),end="")
        print("* "*i)
        

def main():
    print("Enter the Number of rows : ")
    iRow = int(input())

    DisplayPattern(iRow)
    
if __name__ == "__main__":
    main()
