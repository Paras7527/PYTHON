#    A B C D
#X = 1 2 3 6
#Y = 2 3 1 5 
import numpy as np
import math

def EucDistance(P1,P2):     #Distance formula
    Ans = math.sqrt(((P1['x']-P2['x'])**2) + ((P1['y']-P2['y'])**2))
    return Ans

def CalculateDistance(data,line,new_point):
    #Calculate the Distances 
    for d in data:
        d['distance'] = EucDistance(d,new_point)

    print(line)
    print("Calculated Distances are : ")
    for d in data :
        print(d)

def Sorting(data,line):
    #Sort by distance :
    sorted_data = sorted(data,key= lambda item : item['distance'])
    print(line)
    print("Sorted data is :")
    print(line)

    for d in sorted_data : 
        print(d)
    
    k = 9
    nearest = sorted_data[:k]
    print(line)
    print("Sorted 3 elements are :")
    for d in nearest : 
        print(d)
    print(line)

def Voting(nearest,line):
    #Voting
    votes = {}
    for neighbour in nearest : 
        label = neighbour['label']
        votes[label]=(votes.get(label,0)+1)

    print(line)
    print("Result of Voting is : ")
    print(line)
    for d in votes :
        print("Name  :",d,"Value :",votes[d])
    print(line)

def Predict(votes):
    predicted_class = max(votes,key=votes.get)
    print("Predicted class for point (7,5) is :",predicted_class)


def KNN():                  #K Nearest Algo
    line="-"*46
    data = [{'point':'A','x':1,'y':2,'label':'Red'},
            {'point':'B','x':2,'y':3,'label':'Red'},
            {'point':'C','x':1,'y':5,'label':'Red'},
            {'point':'D','x':4,'y':2,'label':'Red'},
            {'point':'E','x':8,'y':6,'label':'Blue'},
            {'point':'F','x':4,'y':5,'label':'Blue'},
            {'point':'G','x':3,'y':7,'label':'Blue'},
            {'point':'H','x':6,'y':5,'label':'Blue'},
            {'point':'I','x':2,'y':9,'label':'Green'},
            {'point':'J','x':10,'y':3,'label':'Green'},
            {'point':'K','x':5,'y':11,'label':'Green'},
            {'point':'L','x':12,'y':3,'label':'Green'}]
            

    print(line)
    print("Training data set :")
    print(line)

    for i in data : 
        print(i)
    print(line)

    new_point = {'x':7,'y':7}

def main():
    print("-------------Demostration of KNN algorithm------------")
    
    KNN()

if __name__ == "__main__":
    main()

#dry run 
#add the data size
#change prediction
#binary -> multiclass
#seperate function