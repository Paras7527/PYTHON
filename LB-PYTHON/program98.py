#Data Structure : Singly Linear Linked List
class Node : 
    def __init__(self,No):
        self.Data = No
        self.next = None

class SinglyLL:
    def __init__(self):
        self.First = None
        self.iCount = 0

################################################################################
    def InsertFirst(self,No):
        newn = Node(No)
        if(self.First == None):     #LL is Empty
            self.First = newn
        else:                       #LL contains atleast one node
            newn.next = self.First
            self.First = newn
        self.iCount += 1
################################################################################

################################################################################
    def InsertAtPos(self):
        pass
################################################################################

################################################################################
    def InsertLast(self):
        pass
################################################################################

################################################################################

################################################################################
    def Display(self):
        temp = self.First
        while(temp!=None):
            print("|",temp.Data,"| -> ",end="")
            temp = temp.next
        print(" None")
################################################################################

################################################################################
    def Count(self):
        return self.iCount
################################################################################



def main():
    print("----------------------------------------------------------------------------")
    print("----------------Demonstartion of Singly Linear Linked List------------------")
    print("----------------------------------------------------------------------------")

    sobj = SinglyLL()

    sobj.InsertFirst(51)
    sobj.InsertFirst(21)
    sobj.InsertFirst(11)

    sobj.Display()

    iRet = sobj.Count()
    print("Number of Node in the Linked list are : ",iRet)
    
if __name__ == "__main__":
    main()
