#Dictionary

#Syntax: {Key : Value}

#Hetrogeneous
#Ordered 
#Indexed    [Not a Numeric]
#Data of Value is Mutable
#Key Duplicate Allowed But Old gets OverWritten
#Value Duplicate Allowed

data={"Name":"Let us C","Author":"Y Kanetkar","Price":340,"Publication":"BPB Publication"}

print("Loop to display Keys")
for X in data:
    print(X)

print("Loop to Display Values")
for X in data.values():
    print(X)

print("Loop to display Key and Value")
for X,Y in data.items():
    print(X," : ",Y)