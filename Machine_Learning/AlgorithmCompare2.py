from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def MarvellousCalculateAccuracyDecisionTree():
    iris = load_iris()

    data = iris.data
    target = iris.target

    X_train,X_test,Y_train,Y_test = train_test_split(data,target,test_size=0.5,random_state=42)

    model = tree.DecisionTreeClassifier()

    model.fit(X_train,Y_train)

    Prediction = model.predict(X_test)

    Accuacy = accuracy_score(Y_test,Prediction)
    return Accuacy

def MarvellousCalculateAccuracyKNN():
    iris = load_iris()

    data = iris.data
    target = iris.target

    X_train,X_test,Y_train,Y_test = train_test_split(data,target,test_size=0.5,random_state=42)

    model = KNeighborsClassifier()

    model.fit(X_train,Y_train)

    Prediction = model.predict(X_test)

    Accuacy = accuracy_score(Y_test,Prediction)
    return Accuacy

def main():
    ret = MarvellousCalculateAccuracyDecisionTree()
    print("Accuracy of Decision Tree Classifier is : ",ret*100)

    et = MarvellousCalculateAccuracyKNN()
    print("Accuracy of KNN is : ",ret*100)

if __name__ == "__main__":
    main()
