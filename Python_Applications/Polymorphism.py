#Method overloading is not allowed in python
#Method Overloading = Not Allowed!
class Demo:
    def Add(A,B):
        return A+B
    
    def Add(A,B,C):
        return A+B+C
    
obj=Demo()

print(obj.Add(10,11))
print(obj.Add(10,11,21))