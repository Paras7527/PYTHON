import sys

def main():
    Border="-"*51
    print(Border)                                                       #Header
    print("-------------Marvellous Automation-----------------")
    print(Border)

    if(len(sys.argv)==2):
        if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
            print("This application is used to perform .........")
            print("This is the Automation script")
        
        elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
            print("Use the given script as .........")
            print("ScriptName.py  Argument1  Argument2")

        else:
            print("Use the given flags as : ")
            print("--h : Used to Display the Help")
            print("--u : Used to Display the Usage")

    else:
        print("Invalid Number of Command Line Arguments!!!")
        print("Use the given flags as : ")
        print("--h : Used to Display the Help")
        print("--u : Used to Display the Usage")

    print(Border)                                                       #Footer
    print("-----------Thank for using our script--------------")
    print("-------------Marvellous Infosystems----------------")
    print(Border)


if __name__=="__main__":
    main()