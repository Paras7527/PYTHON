class Circle:
    PI=3.14
    def __init__(self,A):
        print("Inside Circle Constructor")
        self.Radius=A
    
    def CalculateArea(self):
        Ans=0.0
        Ans=Circle.PI * self.Radius * self.Radius
        return Ans

class CircleX(Circle):
    def __init__(self,A):
        print("Inside CircleX Constructor")
        super().__init__(A)

    def CalculateCircumference(self):
        Ans=0.0
        Ans=2 * Circle.PI * self.Radius
        return Ans

def main():
    obj=CircleX(10.5)
    ret=obj.CalculateArea()
    print("Area of Circle is :",ret)

    ret=obj.CalculateCircumference()
    print("Circumferenece of Circle is :",ret)

if __name__=="__main__":
    main()

#Calling the Special function explicitly is possible in python