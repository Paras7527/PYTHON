#Problems on List / Array (N Numbers)
def Replace(data):
    for i in range(len(data)):
        if(data[i]=='a'):
            data[i] += '_'  #Error!!!
def main():
    print("Enter the String : ")
    str = input()

    iRet = Replace(str)
    print("Frequency is : ",iRet)
    
if __name__ == "__main__":
    main()
