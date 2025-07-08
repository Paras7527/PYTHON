import multiprocessing
import time
import os

def SumEven(no):
    print("PID of SumEven task is : ",os.getpid())
    print("PID of SumEven Process is : ",os.getppid())      #101
    sum=0
    for i in range(0,no+1,2):
        sum=sum+i
    print(sum)

def SumOdd(no):
    print("PID of SumOdd task is : ",os.getpid())
    print("PID of SumOdd Process is : ",os.getppid())       #101
    sum=0
    for i in range(1,no+1,2):
        sum=sum+i
    print(sum)

def main():
    print("Demonstration of Parallel Excution : ")
    print("PID of main process is :",os.getpid())           #101

    start_time=time.time()

    T1=multiprocessing.Process(target=SumEven,args=(900000000,))
    T2=multiprocessing.Process(target=SumOdd,args=(900000000,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    end_time=time.time()

    print("Time Requeired for execution is : ",end_time-start_time)    

    print("End of Application!!!")

if __name__ == "__main__":
    main()