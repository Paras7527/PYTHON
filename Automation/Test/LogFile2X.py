import sys
import time

def main():
    timestam=time.ctime()       #overall time

    Border="-" * 51

    FileName="MarvellousLog%s.log" %(timestam)
    FileName=FileName.replace(" ","_")
    FileName=FileName.replace(":","_")

    print(FileName)

    fobj=open(FileName,"w")

    fobj.write(Border+"\n")
    fobj.write("This is a log file of marvellous automations script\n")
    fobj.write(Border+"\n")

    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    fobj.write(Border+"\n")
    fobj.write("This is created at : \n"+timestam+"\n")
    fobj.write(Border+"\n")

if __name__=="__main__":
    main()