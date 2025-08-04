#Problems on List / Array (N Numbers)
def CountVowel(data):
    ch='a'
    iCount = 0
    for ch in data:
        if(ch == 'a'or ch =='e'or ch=='i'or ch=='o'or ch=='u'):
            iCount = iCount + 1
    return iCount

def main():
    print("Enter the String : ")
    str = input()

    iRet = CountVowel(str)
    print("Frequency is : ",iRet)
    
if __name__ == "__main__":
    main()
