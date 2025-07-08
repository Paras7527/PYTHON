from sklearn import tree

#rough=0
#smooth=1
#tennis 1
#cricket 2
def main():
    BallFeatures = [[35,0],[47,0],[90,1],[48,0],[90,1],[35,0],[92,1],[35,0],[35,0],[35,0]]#encoding
    
    BallNames = [1,1,2,1,2,1,2,1,1,1]#Encoding
    
    obj=tree.DecisionTreeClassifier()#algorithm

    obj=obj.fit(BallFeatures,BallNames) #Train

    print(obj.predict([[93,1]]))#test

if __name__ == "__main__" :
    main()