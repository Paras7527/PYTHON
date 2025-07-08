import os
def main():
    print("Enter the name of file that you want to Delete : ")
    FileName=input()

    ret=os.path.exists(FileName)
    if(ret==True):
        print("File Exists!")
        os.remove(FileName)
    else:
        print("File Doesn't Exists!")
    
if __name__=="__main__":
    main()