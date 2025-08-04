#Problems on Pattern Printing
#row = 5 col = 4
#      ____*____
#      ___* *___
#      __* * *__
#      _* * * *_

def DisplayPattern(row):
    
    for i in range(1,row+1):
        print(" "*(row-i),end="")
        print("* "*i)

def main():
    print("Enter the Number of rows : ")
    iRow = int(input())

    DisplayPattern(iRow)
    
if __name__ == "__main__":
    main()
