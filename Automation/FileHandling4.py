import os
def main():
    print("Enter the name of file that you want to check : ")
    FileName=input()

    ret=os.path.exists(FileName)
    if(ret==True):
        print("File Exists !")
    else:
        print("File Doesn't Exists !")
    
if __name__=="__main__":
    main()