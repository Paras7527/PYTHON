import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn import metrics

def MarvellousAdvertise(Datapath):
    Line = "*"*80

    df = pd.read_csv(Datapath)
    print("Data set : ")
    print(df.head())

    print("Clean the dataset : ")
    df.drop(columns = ["Unnamed: 0"],inplace = True)    # to remove

    print("Updated dataset is : ")
    print(df.head())

    print("Missing values in each column :",df.isnull().sum())

    print("Statistical Summary : \n",df.describe())

    print("Corelation Matrix : ")
    print(df.corr())

    plt.figure(figsize=(10,5))
    sns.heatmap(df.corr(),annot=True,cmap='coolwarm')
    plt.title("Marvellous Corelation Heat Map")
    plt.show()

    sns.pairplot(df)
    plt.suptitle("Pairplot of Features",y=1.02)
    plt.show()
def main():
    MarvellousAdvertise("Advertising.csv")
if __name__ == "__main__":
    main()