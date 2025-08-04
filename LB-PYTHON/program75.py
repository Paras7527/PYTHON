#Problems on Pattern Printing
#HELLO
#H  E   L   L   O
#H  E   L   L   O
#H  E   L   L   O
#H  E   L   L   O
#H  E   L   L   O

def DisplayPattern(data):
    for i in range(len(data)):
        for ch in data:
            print(ch,end="\t")
        print()

def main():
    print("Enter the String : ")
    str = input()

    DisplayPattern(str)
    
if __name__ == "__main__":
    main()
