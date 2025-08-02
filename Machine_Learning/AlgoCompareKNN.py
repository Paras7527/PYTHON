from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def MarvellousCalculateAccuracyKNN():
    iris = load_iris()

    data = iris.data
    target = iris.target

    X_train,X_test,Y_train,Y_test = train_test_split(data,target,test_size=0.5,random_state=42)


    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train,Y_train)
    Prediction = model.predict(X_test)
    Accuacy = accuracy_score(Y_test,Prediction)
    print("Accuarcy is : ",Accuacy*100)



    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X_train,Y_train)
    Prediction = model.predict(X_test)
    Accuacy = accuracy_score(Y_test,Prediction)
    print("Accuarcy is : ",Accuacy*100)



    model = KNeighborsClassifier(n_neighbors=7)
    model.fit(X_train,Y_train)
    Prediction = model.predict(X_test)
    Accuacy = accuracy_score(Y_test,Prediction)
    print("Accuarcy is : ",Accuacy*100)

def main():
    MarvellousCalculateAccuracyKNN()


if __name__ == "__main__":
    main()
