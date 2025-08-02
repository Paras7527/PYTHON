#Logistic Regression

import pandas as pd
import numpy as np 

from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import StandardScaler

def Titanic(Datapath):
    df = pd.read_csv(Datapath)

    print("Dataset Loaded Succesfully!!!")
    print(df.head())
    
    print("Dimensions of Dataset is :",df.shape)

    #Drop
    df.drop(columns = ['Passengerid','zero'],inplace=True)
    print("Dimensions of Updated Dataset",df.shape)

    #Fill the empty space
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])


    plt.figure()
    target = "Survived"
    sns.countplot (data = df,x = target,color='orange',hue='Survived').set_title("Survived vs Non Survived")
    #plt.show()

    plt.figure()
    target = "Survived"
    sns.countplot(data = df,x=target,hue= 'Sex').set_title("based on gender")
    #plt.show()

    plt.figure()
    target = "Survived"
    sns.countplot(data = df,x=target,hue= 'Pclass').set_title("based on Pclass")
    #plt.show()

    plt.figure()
    df['Age'].plot.hist().set_title("Age Report")
    #plt.show()

    plt.figure()
    df['Fare'].plot.hist().set_title("Fare Report")
    #plt.show()

    #Correlation 
    plt.figure(figsize=(10,6))
    sns.heatmap(df.corr(),annot=True,cmap='coolwarm')
    plt.title("Feature correlation heatmap")
    #plt.show()

    x = df.drop(columns = ['Survived'])
    y = df['Survived']

    print("Dimensions of Target :",x.shape)
    print("Dimensions of Labels :",y.shape)

    #Standard Scaler
    scaler = StandardScaler()
    x_scale = scaler.fit_transform(x)

    x_train,x_test,y_train,y_test = train_test_split(x_scale,y,test_size=0.2,random_state=42)

    model = LogisticRegression()

    model.fit(x_train,y_train)

    y_predict = model.predict(x_test)

    Accuracy = accuracy_score(y_test,y_predict)
    print("Accuracy is :",Accuracy*100)

    cm = confusion_matrix(y_test,y_predict)
    print("Confusion matrix is : \n",cm)

    importance = pd.Series(model.feature_importances_,index=x.columns)
    importance = importance.sort_values(ascending=False)

    importance.plot(kind='bar',figsize=(10,6),title="Feature importance")
    plt.show()
    
def main():
    Titanic("MarvellousTitanicDataset.csv")

if __name__ == "__main__":
    main()