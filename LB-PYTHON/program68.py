#Problems on List / Array (N Numbers)
def StrUpr(data):
    output = ""
    for ch in data :
        if(ch>='a' and ch<='z'):
            output = output + chr(ord(ch) - 32) 
        else:
            output = output + ch
    return output

def main():
    print("Enter the String : ")
    str = input()

    iRet = StrUpr(str)
    print("Frequency is : ",iRet)
    
if __name__ == "__main__":
    main()
