import pandas as pd
import numpy as np 

from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt
import seaborn as sns

def Wine_Predictor(Datapath):
    df = pd.read_csv(Datapath)

    #To Drop missing values
    df.dropna(inplace=True)

    x = df.drop(columns = ['Class'])
    y = df['Class']

    scaler = StandardScaler()
    x_scale = scaler.fit_transform(x)

    x_train,x_test,y_train,y_test = train_test_split(x_scale,y,test_size=0.2,random_state=42)

    Accuracy_Scores = []
    k_range = range(1,21)

    #Parameter Tuning
    for k in k_range: 
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(x_train,y_train)
        y_predict = model.predict(x_test)
        Accuracy = accuracy_score(y_test,y_predict)
        Accuracy_Scores.append(Accuracy)

    plt.figure(figsize=(8,5))
    plt.plot(k_range,Accuracy_Scores,marker = 'o',linestyle = '--')
    plt.title("Accuracy vs K_Value")
    plt.xlabel("Value of K")
    plt.ylabel("Accuracy of model")
    plt.grid(True)
    plt.xticks(k_range)
    plt.show()

    best_k = k_range[Accuracy_Scores.index(max(Accuracy_Scores))]
    print("Best value of k is : ",best_k)

    model = KNeighborsClassifier(n_neighbors=best_k)
    model.fit(x_train,y_train)
    y_predict = model.predict(x_test)
    Accuracy = accuracy_score(y_test,y_predict)
    print("Final Accuracy score is : ",Accuracy*100)

    conf_matrix = confusion_matrix(y_test,y_predict)
    print("Confusion matrix is : \n",conf_matrix)

def main():
    Wine_Predictor("WinePredictor.csv")

if __name__ == "__main__":
    main()