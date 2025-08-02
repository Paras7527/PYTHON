import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

def DiabetesPrediction(Datapath):
    df = pd.read_csv(Datapath)

    print("Data Loaded Successfully!!!")
    print(df.head())

    print("The Shape of the Database : ")
    print(df.shape)

    print('The description about the database : ')
    print(df.describe())

    x = df.drop(columns=['Outcome'])
    y = df['Outcome']

    print("The Shape of x :\n",x.shape)
    print("The Shape of y :\n",y.shape)

    scaler = StandardScaler()
    x = scaler.fit_transform(x)

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

    model = LogisticRegression()

    model.fit(x_train,y_train)

    y_prediction = model.predict(x_test)

    accuracy = accuracy_score(y_test,y_prediction)

    print("The accuracy is : ",accuracy)


def main():

    DiabetesPrediction("diabetes.csv")

if __name__ == "__main__":
    main()