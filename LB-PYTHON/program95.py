#Data Structure : Singly Linked List

class Arithematic :
    def __init__(self,A = 0,B = 0):
        print("Inside Constructor")
        self.No1 = A
        self.No2 = B

    

def main():
    print("Inside Main")

    obj1 = Arithematic(11,10)

    iRet1 = obj1.Addition()
    iRet2 = obj1.Substraction()
    iRet3 = obj1.Multiplication()
    iRet4 = obj1.Division()

    print("Addition is :",iRet1)
    print("Substraction is :",iRet2)
    print("Multiplication is :",iRet3)
    print("Division is :",iRet4)

if __name__ == "__main__":
    main()
