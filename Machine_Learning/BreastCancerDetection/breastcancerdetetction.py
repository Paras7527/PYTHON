import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier


def BreastCancerDetetction(Datapath):
    Line = "*"*128
    
    df = pd.read_csv(Datapath)

    print(Line)
    print("The first five records of the Dataset are : ")
    print(df.head())
    print(Line)

    print("The Total Rows and Column in the Dataset are : ")
    print(df.shape)
    print(Line)

    print("The Overall Description of the dataset is : ")
    print(df.describe())
    print(Line)

    #The CodeNumber is not an effective topic in the Dataset so we have to remove/drop it!

    df.drop(columns=['CodeNumber'],inplace = True , axis=1)
    print("The Unwanted Column Dropped Successfully!!!")
    print("The Shape of the updated dataset is : ")
    print(df.shape)
    print(Line)

    #There are some Blank spaces in the code so we have to remove it
    df = df.apply(lambda col: pd.to_numeric(col, errors='coerce'))
    df = df.fillna(df.mean())
    print("DataFrame after removing rows with missing values:")
    print(Line)
    print(df.head())
    print(Line)

    #Now we have to split the independent and dependent columns of datasets
    x = df.drop(columns=['CancerType'])
    y = df['CancerType']

    scaler = StandardScaler()
    x_scale = scaler.fit_transform(x)

    #Now we have to split the dataset into four parts 
    x_train,x_test,y_train,y_test = train_test_split(x_scale,y,test_size=0.2,random_state=42)

    #Now we have to train test the model and find the accuracy

    model = LogisticRegression()           #97.14
    #model = DecisionTreeClassifier()       95.71

    model.fit(x_train,y_train)

    y_predict = model.predict(x_test)

    accuracy  = accuracy_score(y_test,y_predict)
    print("The Accuracy of the model is : ")
    print(accuracy*100)
    print(Line)

def main():
    BreastCancerDetetction("breastcancerdataset.csv")

if __name__ == "__main__":
    main()