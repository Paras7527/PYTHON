#Writing Our Own Logic : 
def Increase(A):
    return A+1

def Demo(Task,Value):
    result=[]
    for no in Value:
        ret=Task(no)
        result.append(ret)

    return result

Data=[13,17,10,14,11]

RData=Demo(Increase,Data)
print(RData)