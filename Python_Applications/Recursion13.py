#Input = 4 .    Output = 10 4+3+2+1
Fact=1
def Factorial(no):
    global Fact
    if(no>=1):
        Fact=Fact*no
        no=no-1
        Factorial(no)
    return Fact
    
def main():
    iRet=Factorial(4)
    print(iRet)
    
if __name__=="__main__":
    main()