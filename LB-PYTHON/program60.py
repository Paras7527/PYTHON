#Problems on List / Array (N Numbers)
def CountNonVowel(data):
    iCount = 0

    pattern = "aeiouAEIOU"
    for ch in data :
        if(ch not in pattern):
            iCount = iCount + 1
    return iCount

def main():
    print("Enter the String : ")
    str = input()

    iRet = CountNonVowel(str)
    print("Frequency is : ",iRet)
    
if __name__ == "__main__":
    main()
