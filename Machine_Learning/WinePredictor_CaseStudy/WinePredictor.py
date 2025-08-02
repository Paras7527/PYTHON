import pandas as pd
import numpy as np 

from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import StandardScaler

def Wine_Predictor(Datapath):
    df = pd.read_csv(Datapath)

    print("Dataset Loaded Succesfully!!!")
    print(df.head())
    
    print("Dimensions of Dataset is :",df.shape)

    #To Drop missing values
    df.dropna(inplace=True)

    x = df.drop(columns = ['Class'])
    y = df['Class']

    scaler = StandardScaler()
    x_scale = scaler.fit_transform(x)

    x_train,x_test,y_train,y_test = train_test_split(x_scale,y,test_size=0.2,random_state=42)

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(x_train,y_train)

    y_predict = model.predict(x_test)

    Accuracy = accuracy_score(y_test,y_predict)
    print("Accuracy is :",Accuracy*100)

def main():
    Wine_Predictor("WinePredictor.csv")

if __name__ == "__main__":
    main()