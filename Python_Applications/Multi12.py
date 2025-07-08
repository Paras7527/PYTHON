import os

def Fun(no):
    sum=0
    for i in range(1,no):
        sum=sum+(i*i*i)
    return sum
def main():
    ret=Fun(100)
    print(ret)
if __name__ == "__main__":
    main()