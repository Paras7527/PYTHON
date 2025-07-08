pi = 3.14

def CircleArea(Rad):
    Area = pi * Rad * Rad
    return Area

def main() :
    print("Enter the Radius of Circle : ")
    Radius = float(input())
    
    fRet=CircleArea(Rad = Radius)   #Keyword Arguments
    print("Area of Circle is : " , fRet)
    
if __name__ == "__main__" :
    main()