
def main():
    print("Enter the name of file that you want to create : ")
    FileName=input()

    fobj=open(FileName,"w")

    print("Enter the data that you want to write in file : ")
    Data=input()

    fobj.write(Data)

    fobj.close()
    
if __name__=="__main__":
    main()