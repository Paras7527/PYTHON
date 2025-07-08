import threading
import time

def SumEven(no):
    sum=0
    for i in range(0,no+1,2):
        sum=sum+i
    print(sum)

def SumOdd(no):
    sum=0
    for i in range(1,no+1,2):
        sum=sum+i
    print(sum)

def main():
    print("Demonstration of Serial Excution : ")

    start_time=time.time()

    ret1=SumEven(900000000)
    ret2=SumOdd(900000000)

    print("Sum of even : ",ret1)
    print("Sum of odd : ",ret2)

    end_time=time.time()

    print("Time Requeired for execution is : ",end_time-start_time)

    print("End of Application!!!")


    
if __name__ == "__main__":
    main()