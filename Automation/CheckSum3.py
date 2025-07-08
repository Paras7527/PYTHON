import hashlib

def CalculateCheckSum(path,BlockSize = 1024):
    fobj = open(path,'rb')

    hobj = hashlib.md5()

    buffer = fobj.read(BlockSize)

    while(len(buffer)>0):
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)

    fobj.close()

    return hobj.hexdigest()

def main():
    print("Enter the File Name : ")
    FileName = input()

    ret = CalculateCheckSum(FileName)
    print("CheckSum of File is : " , ret)

if __name__ == "__main__" :
    main()