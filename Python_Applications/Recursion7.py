#Input = 4 .    Output = *   *   *   *
def Display(no):
    i=1
    while(i<=no):
        print("*",end="  ")
        i=i+1
    print()

def main():
    Display(4)

if __name__=="__main__":
    main()