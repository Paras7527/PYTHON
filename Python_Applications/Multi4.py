
import threading

def Display():
    print("Inside Display")

def main():
    print("Inside Main")
    T1=threading.Thread(target=Display) #Callback Function
    T1.start()
    
if __name__ == "__main__":
    main()