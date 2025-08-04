#Problems on List / Array (N Numbers)
def CountVowel(data):
    iCount = 0

    pattern = "aeiouAEIOU"
    for ch in data :
        if(ch in pattern):
            iCount = iCount + 1
    return iCount

def main():
    print("Enter the String : ")
    str = input()

    iRet = CountVowel(str)
    print("Frequency is : ",iRet)
    
if __name__ == "__main__":
    main()
