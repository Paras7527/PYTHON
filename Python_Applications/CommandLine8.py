import sys

def Add(No1,No2):
    result=No1+No2
    return result

def main():
    if(len(sys.argv)==2):
        if(sys.argv[1] == "--h"):   #Help
            print("\nThis Application is used to Perform Addition of Two Numbers\n")
            return
    
        if(sys.argv[1] == "--u"):   #Usage
            print("\nExecute the code as\n")
            print("python Filename.py First_Input Second_Input\n")
            return
    
    
    if(len(sys.argv)!=3):
        print("Insufficient number of arguments!")
        print("You can use --h for Help and --u as Usage")
        return 
    
    Value1=int(sys.argv[1])
    Value2=int(sys.argv[2])

    ret=Add(Value1,Value2)
    print("Addition is :",ret)

if __name__ == "__main__":
    main()
