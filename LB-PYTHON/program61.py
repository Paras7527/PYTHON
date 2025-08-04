#Problems on List / Array (N Numbers)
def CountSmall(data):
    iCount = 0
    for ch in data :
        if(ch>='a' and ch<='z'):
            iCount = iCount + 1
    return iCount
        

def main():
    print("Enter the String : ")
    str = input()

    iRet = CountSmall(str)
    print("Frequency is : ",iRet)
    
if __name__ == "__main__":
    main()
