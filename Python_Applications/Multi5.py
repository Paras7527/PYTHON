
import threading

def Display(Value1,Value2):
    print("Inside Display",Value1,Value2)

def main():
    print("Inside Main")
    T1=threading.Thread(target=Display,args=(11,21)) #Callback Function
    T1.start()
    
if __name__ == "__main__":
    main()