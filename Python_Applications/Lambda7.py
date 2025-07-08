def Power(X,Y):
    result=1
    for i in range(Y):
        result=result*X
    return result

ret=Power(10,7)
print("Power of Element is : ",ret)