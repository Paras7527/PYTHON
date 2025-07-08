import sys

def Add(No1,No2):
    result=No1+No2
    return result

def main():
    if(len(sys.argv)!=3):
        print("Insufficient number of arguments!")
        return 
    
    Value1=int(sys.argv[1])
    Value2=int(sys.argv[2])

    ret=Add(Value1,Value2)
    print("Addition is :",ret)

if __name__ == "__main__":
    main()
