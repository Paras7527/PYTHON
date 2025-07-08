#Set

#Syntax: {}

#Hetrogeneous
#UnOrdered 
#UnIndexed
#Set is Mutable
#Data is Immutable
#Duplicate Not Allowed

data={10,90.67,"Hello",True,10}

print("Data type is:",type(data))
print("Length is :",len(data))

#print(data[0])

print(data)

data.add(71)
print(data)

data.remove(10)
print(data)

print("Data using Loop")
for value in data:
    print(value)