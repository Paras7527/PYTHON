import os
def main():
    print("Enter the name of file that you want Read : ")
    FileName=input()

    ret=os.path.exists(FileName)
    if(ret==True):
        print("File Exists!")
        fobj=open(FileName,"r")
        
        data=fobj.read()
        print("Data from file is :",data)

        fobj.close()
    else:
        print("File Doesn't Exists!")
    
if __name__=="__main__":
    main()