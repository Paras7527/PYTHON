def ChkEven(iNo):
    return (iNo%2==0)
    
ret = ChkEven(10)

if ret==True:
    print("Number is Even")
else:
    print("Number is Odd")



checkeven = lambda iNo : iNo%2==0
ret = checkeven(10)
print(ret)