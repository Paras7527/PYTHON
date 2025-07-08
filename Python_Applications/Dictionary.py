#Dictionary

#Syntax: {Key : Value}

#Hetrogeneous
#Ordered 
#Indexed    [Not a Numeric]
#Data of Value is Mutable
#Key Duplicate Allowed But Old gets OverWritten
#Value Duplicate Allowed

data={"Name":"Let us C","Author":"Y Kanetkar","Price":340,"Publication":"BPB Publication"}

print("Data type is:",type(data))
print("Length is",len(data))

print(data)

#print(data[0])
print(data["Author"])

data["Price"]=400
print(data)

