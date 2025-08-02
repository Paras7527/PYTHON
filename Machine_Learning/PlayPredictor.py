#'Sunny' : 0,'Rainy' : 1,'Overcast' : 2
#'Hot' : 10,'Cool' : 20,'Mild' : 30
#'Yes': 100, 'No':200

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score,mean_squared_error,root_mean_squared_error,accuracy_score

def PlayPredictorCaseStudy(Dataset):
    Line = "*"*80

    df = pd.read_csv(Dataset)

    #Drop the Column
    print(Line)
    print("Clean the Dataset : ")
    df.drop(columns=["Unnamed: 0"],inplace = True)

    #Encoding
    print(Line)
    df['Whether'] = df['Whether'].map({'Sunny' : 0,'Rainy' : 1,'Overcast' : 2})

    df['Temperature'] = df['Temperature'].map({'Hot' : 10,'Cool' : 20,'Mild' : 30})

    df['Play'] = df['Play'].map({'Yes': 100, 'No':200})
    
    print("The Encoded Dataset is : ")
    print(df.head())

    print(Line)
    print("Statistical Summary : ")
    print(Line)
    print(df.describe())
    print(Line)

    print("Corelation Matrix : ")
    print(Line)
    print(df.corr())

    print(Line)
    print("Heat Map : ")
    print(Line)
    plt.figure(figsize=(10,5))
    sns.heatmap(df.corr(),annot=True,cmap='coolwarm')
    plt.title("Marvellous Corelation Heat Map")
    plt.show()
    
    print("Pairplot : ")
    print(Line)
    sns.pairplot(df)
    plt.suptitle("Pairplot of Features",y=1.02)
    plt.show()

    x = df[['Whether','Temperature']]
    y = df['Play']

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

    model = LogisticRegression()

    model.fit(x_train,y_train)

    y_predict = model.predict(x_test)

    accuracy = accuracy_score(y_test,y_predict)
    print("Accuracy is : ",accuracy*100)

def main():
    PlayPredictorCaseStudy("PlayPredictor.csv")

if __name__ == "__main__":
    main()