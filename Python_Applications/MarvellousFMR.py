def filterX(Task,Values):
    Result=[]
    for no in Values:
        #Result.append(Task(no))
        ret=Task(no)
        if(ret==True):
            Result.append(no)  

    return Result

def mapX(Task,Values):
    Result=[]
    for no in Values:
        ret=Task(no)
        Result.append(ret)

    return Result

def reduceX(Task,Values):
    #[11, 13, 5, 7, 9, 13, 17]
    Result=0
    for no in Values:
        Result=Task(Result,no)

    return Result