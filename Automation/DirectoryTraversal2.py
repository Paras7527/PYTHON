import os
def Directorywatcher():
    for FolderName , SubFolderNames , FileNames in os.walk("Marvellous"):
        print("Folder Name is : "+FolderName)

        for subf in SubFolderNames:
            print("Sub folder name is : "+subf)

        for fname in FileNames:
            print("File name is : "+fname)
def main():
    Directorywatcher()
if __name__=="__main__":
    main()