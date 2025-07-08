import os
import sys

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
    TotalCount=0
    EmptyCount=0
    for FolderName , SubFolderNames , FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            TotalCount = TotalCount + 1
            if(os.path.getsize(os.path.join(FolderName,fname))==0):
                EmptyCount = EmptyCount + 1
                print("File name is : "+fname)
                os.remove(os.path.join(FolderName,fname))

    print("The total number of files Scanned : ",TotalCount)
    print("Total number of empty files detected : ",EmptyCount)
                
def main():
    Border="-"*51
    print(Border)                                                       #Header
    print("-------------Marvellous Automation-----------------")
    print(Border)

    if(len(sys.argv)==2):
        if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
            print("This application is used to perform Directory Cleaning")
            print("This is the Directory Automation script")
        
        elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
            print("Use the given script as .........")
            print("ScriptName.py  NameofDirectory")
            print("Please provide valid absolute path")

        else:
            Directorywatcher(sys.argv[1])

    else:
        print("Invalid Number of Command Line Arguments!!!")
        print("Use the given flags as : ")
        print("--h : Used to Display the Help")
        print("--u : Used to Display the Usage")

    print(Border)                                                       #Footer
    print("-----------Thank for using our script--------------")
    print("-------------Marvellous Infosystems----------------")
    print(Border)





if __name__=="__main__":
    main()

