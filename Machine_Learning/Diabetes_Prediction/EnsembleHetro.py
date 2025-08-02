#Class !!
#Parallel Working = Bagging[Hetrogeneous]
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier

def main():
    df = pd.read_csv("diabetes.csv")

    x = df.drop(columns = ['Outcome'])
    y = df['Outcome']

    scaler = StandardScaler()
    x_scale = scaler.fit_transform(x)

    x_train,x_test,y_train,y_test = train_test_split(x_scale,y,test_size=0.2,random_state=42)

    log_clf = LogisticRegression()
    dt_clf = DecisionTreeClassifier(max_depth = 10)
    knn_clf = KNeighborsClassifier(n_neighbors=5)

    voting_clf = VotingClassifier(
        estimators=[
            ('lr',log_clf),
            ('dt',dt_clf),
            ('knn',knn_clf)
        ],
        voting='hard'
    )

    voting_clf.fit(x_train,y_train)

    y_predict = voting_clf.predict(x_test)

    Accuracy = accuracy_score(y_test,y_predict)
    print("The Accuaracy of Model is : ",Accuracy*100)

if __name__ == "__main__":
    main()