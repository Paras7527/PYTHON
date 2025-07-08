import os

def main():
    print("PID of Current Process : ",os.getpid())

    print("PID of Parent Process : ",os.getppid())
    
if __name__ == "__main__":
    main()