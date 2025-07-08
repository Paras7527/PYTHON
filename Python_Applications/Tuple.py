#Tuple

#Syntax: ()

#Hetrogeneous
#Ordered 
#Indexed
#Data Immutable
#Tuple Immutable
#Duplicate Allowed

data=(10,"Hello",90.67,True,10)
print("DataType is : ",type(data))
print("Length is : ",len(data))

print(data)

print(data[0])
print(data[1])

#data[0]=11
print(data)

print("Data Display using Loop")
for value in data:
    print(value)

for i in range(len(data)):
    print(data[i])