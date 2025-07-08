#Input = 4 .    Output = 10 4+3+2+1
i=1
def Add(no):
    sum=0
    while(no>=1):
        sum=sum+no
        no=no-1
    return sum
    
def main():
    iRet=Add(4)
    print(iRet)
    
if __name__=="__main__":
    main()