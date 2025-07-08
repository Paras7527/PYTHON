no=11

def fun():
    global no
    x=21
    print("Inside Fun")
    print("Value of X is : ",x)
    no=no+1
    print("Value of no : ",no)

def main():
    print("Value of no before FUN : ",no)
    fun()
    print("Value of no after FUN : ",no)

if __name__ == "__main__":
    main()