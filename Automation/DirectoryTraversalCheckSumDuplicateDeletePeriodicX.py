import os
import sys
import time
import hashlib
import schedule
import Email1

def CalculateChecksum(path, BlockSize = 1024):
    fobj = open(path,'rb')

    hobj = hashlib.md5()

    buffer = fobj.read(BlockSize)
    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)

    fobj.close()

    return hobj.hexdigest()

def DirectoryWatcher(DirectoryName = "Marvellous"):

    flag = os.path.isabs(DirectoryName)

    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if(flag == False):
        print("Path is valid but the target is not a directory")
        exit()

    for FolderName , SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname = os.path.join(FolderName,fname)
            checksum = CalculateChecksum(fname)
            print("File name : ",fname)
            print("Checksum : ",checksum)
            print()

    timestamp = time.ctime()

    filename = "MarvellousLog%s.log" %(timestamp)
    filename = filename.replace(" ","_")
    filename = filename.replace(":","_")

    filepath = LogDirectory(filename)

    fobj = open(filepath,"w")

    Border = "-"*54
    
    fobj.write(Border+"\n")
    fobj.write("This is a log file of Marvellous Automation Script\n")
    fobj.write("This is a Driectory Cleaner Script\n")

    fobj.write(Border+"\n")

    fobj.write(Border+"\n")
    fobj.write("This is is created at \n"+timestamp+"\n")
    fobj.write(Border+"\n")

def FindDuplicate(DirectoryName = "Marvellous"):

    flag = os.path.isabs(DirectoryName)

    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if(flag == False):
        print("Path is valid but the target is not a directory")
        exit()

    Duplicate = {}

    for FolderName , SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname = os.path.join(FolderName,fname)
            checksum = CalculateChecksum(fname)

            if checksum in Duplicate:
                Duplicate[checksum].append(fname)
            else:
                Duplicate[checksum] = [fname]

    return Duplicate

def DisplayResult(MyDict):
    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    Count = 0

    for value in Result:
        for subvalue in value:
            Count = Count + 1
            print(subvalue)
        print("-------------------------------")
        print("Value of Count is : ",Count)
        print("-------------------------------")
        Count = 0

def DeleteDuplicate(Path = "Marvellous"):
    timestam=time.ctime()

    MyDict = FindDuplicate(Path)
    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    FileName="MarvellousLog%s.log" %(timestam)
    FileName=FileName.replace(" ","_")
    FileName=FileName.replace(":","_")

    FilePath = LogDirectory(FileName)

    Count = 0
    Cnt = 0

    fobj=open(FilePath, "w")
    Border = "-" * 60
    fobj.write(Border + "\n")
    fobj.write("Marvellous Automation - Duplicate File Deletion Log\n")
    fobj.write("Log created at: %s\n" % timestam)
    fobj.write(Border + "\n\n")

    for value in Result:
        for subvalue in value:
            Count = Count + 1
            if Count > 1:
                try:
                    os.remove(subvalue)
                    Cnt=Cnt+1
                    fobj.write("Deleted File: %s\n" % subvalue)
                except Exception as e:
                    DeletedCount = DeletedCount + 1
                    fobj.write("deleting file: %s | Reason: %s\n" % (subvalue, str(e)))
        Count = 0

    print("Total deleted file : ",Cnt)
    print("Log file created: ", FilePath)

def CreateLog():
    timestam=time.ctime()       #overall time

    Border="-" * 51
    
    FileName="MarvellousLog%s.log" %(timestam)
    FileName=FileName.replace(" ","_")
    FileName=FileName.replace(":","_")

    FilePath = LogDirectory(FileName)

    print(FilePath)

    fobj=open(FilePath,"w")

    fobj.write(Border+"\n")
    fobj.write("This is a log file of marvellous automations script\n")
    fobj.write(Border+"\n")

    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    fobj.write(Border+"\n")
    fobj.write("This is created at : \n"+timestam+"\n")
    fobj.write(Border+"\n")
    
def LogDirectory(FileName):
    folder_name = "Marvellous"
    os.makedirs(folder_name, exist_ok=True)
    return os.path.join(folder_name, FileName)

def main():
    Border = "-"*54
    print(Border)
    print("--------------- Marvellous Automation ----------------")
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform directory cleaning")
            print("This is the directory automation script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py  NameOfDirctory timeinterval")
            print("Please provide valid absolute path")

    if(len(sys.argv) == 3):
            schedule.every(int(sys.argv[2])).minutes.do(DeleteDuplicate)

            while True:
                schedule.run_pending()
                time.sleep(1)

    else:
        print("Invalid number of coomand line arguments")
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage") 

    CreateLog()

    print(Border)
    print("----------- Thank you for using our script -----------")
    print("---------------- Marvellous Infosystems --------------")
    print(Border)

if __name__ == "__main__":
    main()