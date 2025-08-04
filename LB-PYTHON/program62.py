#Problems on List / Array (N Numbers)
def Replace(data):
    iCount = 0
    output = ""
    for ch in data :
        if(ch =='a'):
            output.append('_')      #Error!!!
        else:   
            output.append(ch)


def main():
    print("Enter the String : ")
    str = input()

    iRet = Replace(str)
    print("Frequency is : ",iRet)
    
if __name__ == "__main__":
    main()
