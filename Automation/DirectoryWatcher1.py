import os
def main():
    print("Enter the name of Directory : ")
    DirName=input()

    ret=os.path.isabs(DirName)
    if(ret==True):
        print("Input is absolute path ")
    else:
        print("Input is relative path")
if __name__=="__main__":
    main()

#/Desktop/PYTHON/Automation/Marvellous/AI/X.txt         (Absolute Path = command + shift + G)

#Marvellous/AI/X.txt                                    (Relative Path)