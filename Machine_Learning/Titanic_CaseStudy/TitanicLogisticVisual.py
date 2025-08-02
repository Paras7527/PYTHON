#Logistic Regression

import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

def Titanic(Datapath):
    df = pd.read_csv(Datapath)

    print("Dataset Loaded Succesfully!!!")
    print(df.head())
    
    print("Dimensions of Dataset is :\n",df.shape)

    #Drop
    df.drop(columns = ['Passengerid','zero'],inplace=True)
    print("Dimensions of Updated Dataset",df.shape)

    #Fill the empty space
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])


    plt.figure()
    target = "Survived"
    sns.countplot (data = df,x = target,color='orange',hue='Survived').set_title("Survived vs Non Survived")
    plt.show()

    plt.figure()
    target = "Survived"
    sns.countplot(data = df,x=target,hue= 'Sex').set_title("based on gender")
    plt.show()

    plt.figure()
    target = "Survived"
    sns.countplot(data = df,x=target,hue= 'Pclass').set_title("based on Pclass")
    plt.show()

    plt.figure()
    df['Age'].plot.hist().set_title("Age Report")
    plt.show()

    plt.figure()
    df['Fare'].plot.hist().set_title("Fare Report")
    plt.show()

    

def main():
    Titanic("MarvellousTitanicDataset.csv")

if __name__ == "__main__":
    main()