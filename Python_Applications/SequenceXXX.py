def CircleArea(Rad,pi = 3.14):  #Default Arguments
    Area = pi * Rad * Rad
    return Area

def main() :
    print("Enter the Radius of Circle : ")
    Radius = float(input())
    
    fRet=CircleArea(Radius)
    print("Area of Circle is : " , fRet)
    
if __name__ == "__main__" :
    main()