#HEAD SIZE + BRAIN SIZE = Gender
#LOGISTIC REGRESSION

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def HeadBrainModel(datasetpath):
    df = pd.read_csv(datasetpath)
    print("Dimension of Dataset : ")
    print(df.shape)

    print("Initial data is :")
    print(df.head())

    plt.figure(figsize=(8,6))   #Size is in inch
    sns.scatterplot(data=df, x='Head Size(cm^3)', y='Brain Weight(grams)', hue='Head Size(cm^3)', palette='Set1')
    plt.title("Marvellous Head Brain Model")
    plt.xlabel("Height")
    plt.ylabel("Weight")
    plt.grid(True)
    #plt.show()

    X = df[["Head Size(cm^3)","Brain Weight(grams)","Age Range"]]
    Y = df["Gender"]

    X_train,X_test,Y_train,Y_Test = train_test_split(X,Y,test_size=0.3,random_state=42)

    model = LogisticRegression()

    model.fit(X_train,Y_train)

    Y_Predict = model.predict(X_test)

    accuracy = accuracy_score(Y_Test,Y_Predict)
    print("The total accuracy is : ",accuracy*100)


def main():
    HeadBrainModel("HeadBrain.csv")

if __name__ == "__main__":
    main()