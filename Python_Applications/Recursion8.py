#Input = 4 .    Output = *   *   *   *
i=1
def Display(no):
    global i
    if(i<=no):
        print("*",end="  ")
        i=i+1
        Display(no)
    
def main():
    Display(4)

if __name__=="__main__":
    main()