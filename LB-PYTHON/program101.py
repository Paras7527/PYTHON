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
    def InsertLast(self,No):
        newn = Node(No)
        if(self.First == None):     #LL is Empty
            self.First = newn
        else:                       #LL contains atleast one node
            temp = self.First
            while(temp.next!=None):
                temp = temp.next

            temp.next = newn
        self.iCount += 1
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

################################################################################
    def DeleteFirst(self):
        if(self.First == None):
            return
        else:
            temp = self.First
            self.First = self.First.next
            del temp

            self.iCount = self.iCount - 1
################################################################################

################################################################################
    def DeleteLast(self):
        if(self.First == None):                            #LL is Empty
            return
        elif(self.First.next == None):                     #LL contains One node
            del self.First
            self.First = None
        else:                                              #LL contains more than one node
            temp = self.First
            while(temp.next.next!=None):
                temp = temp.next
            del temp.next
            temp.next = None
        self.iCount = self.iCount - 1
################################################################################

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

    sobj.InsertLast(101)
    sobj.InsertLast(111)
    sobj.InsertLast(121)

    sobj.Display()

    iRet = sobj.Count()
    print("Number of Node in the Linked list are : ",iRet)

    sobj.DeleteFirst()

    sobj.Display()

    iRet = sobj.Count()
    print("Number of Node in the Linked list are : ",iRet)

    sobj.DeleteLast()

    sobj.Display()

    iRet = sobj.Count()
    print("Number of Node in the Linked list are : ",iRet)

################################################################################

    
if __name__ == "__main__":
    main()
