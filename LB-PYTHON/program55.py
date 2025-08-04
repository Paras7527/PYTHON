#Problems on List / Array (N Numbers)
def CountFreq(data):
    ch='a'
    iCount = 0
    for ch in data:
        if(ch == 'a'):
            iCount = iCount + 1
    return iCount

def main():
    print("Enter the String : ")
    str = input()

    iRet = CountFreq(str)
    print("Frequency is : ",iRet)
    
if __name__ == "__main__":
    main()
