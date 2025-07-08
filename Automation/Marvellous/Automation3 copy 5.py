#(pip = pip install packages)
import schedule
import time
import datetime

def MySchedule():
    print("Inside my schedule function at :",datetime.datetime.now())
    
def main():
    print("Inside Automation script")
    print("Current time is : ",datetime.datetime.now())

    schedule.every(5).seconds.do(MySchedule)

    print("Application is in waiting state : ")

    time.sleep(50)

    print("End of Automation script !!!")
if __name__=="__main__":
    main()