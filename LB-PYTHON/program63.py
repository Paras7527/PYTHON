#Problems on List / Array (N Numbers)
def Replace(data):
    output = ""
    for ch in data :
        if(ch =='a'):
            output=output+'_'
        else:   
            output=output+ch
    return output

def main():
    print("Enter the String : ")
    str = input()

    iRet = Replace(str)
    print("Frequency is : ",iRet)
    
if __name__ == "__main__":
    main()
