import os
import hashlib

def main():
    print("Enter the File Name : ")
    FileName=input()

    fobj=open(FileName,'rb')

    hobj=hashlib.md5()

    buffer=fobj.read(1024)

    while(len(buffer)>0):
        hobj.update(buffer)
        buffer=fobj.read(1024)

    fobj.close()

    print("CheckSum of File is :",hobj.hexdigest())
    
if __name__=="__main__":
    main()