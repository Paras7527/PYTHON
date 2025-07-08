import os
def Directorywatcher(DirectoryName="Marvellous"):
    Flag = os.path.isabs(DirectoryName)

    if(Flag == False):
        DirectoryName=os.path.abspath(DirectoryName)

    Flag=os.path.exists(DirectoryName)
    if(Flag==False):
        print("The path is invalid")
        exit()

    Flag=os.path.isdir(DirectoryName)
    if(Flag==False):
        print("Path is valid but target is not a directory")
        exit()

    print("Absolute path is : "+DirectoryName)

    for FolderName , SubFolderNames , FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            print("File name is : "+fname)
            print("File size is : ",os.path.getsize(os.path.join(FolderName,fname))," bytes")

def main():
    print("Enter the name of directory that you want to travel :")
    DirName=input()

    Directorywatcher(DirName)
if __name__=="__main__":
    main()

