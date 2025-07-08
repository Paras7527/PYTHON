import os
def Directorywatcher(DirectoryName):
    for FolderName , SubFolderNames , FileNames in os.walk(DirectoryName):
        print("Folder Name is : "+FolderName)

        for subf in SubFolderNames:
            print("Sub folder name is : "+subf)

        for fname in FileNames:
            print("File name is : "+fname)
def main():
    print("Enter the name of directory that you want to travel :")
    DirName=input()

    Directorywatcher(DirName)
if __name__=="__main__":
    main()