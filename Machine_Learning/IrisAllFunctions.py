import pandas as pd
from sklearn.model_selection import train_test_split

def LoadData(file_path):
    df=pd.read_csv(file_path)
    print("Datasets gets loaded in memory succesfully!")
    return df

def GetInfo(df):
    print("Information about the loaded data set is : ")
    print("Shape of Dataset : ",df.shape)
    print("columns : ",df.columns)
    print("Missing Values : ",df.isnull().sum())

def EncodeData(df):
    df["variety"] = df["variety"].map({"Setosa":0,"Versicolor":1,"Virginica":2})
    return df
    
def split_feature_target(df):
    X=df.drop('variety',axis='column')
    Y=df["variety"]
    return X,Y

def split(X,Y,size=0.2):
    return train_test_split(X,Y,test_size=size)

def train():
    pass

def main():
    data=LoadData("iris.csv")
    print(data.head())

    GetInfo(data)

    print("Data after encoding")
    data=EncodeData(data)
    print(data.head())

    print("Splitting features and labels : ")
    Independent,Dependent = split_feature_target(data)
    print(Independent.head())
    print(Dependent.head())

    X_train,X_test,Y_train,Y_test=split(Independent,Dependent,0.3)
    print(X_train.shape)
    print(X_test.shape)
    print(Y_train.shape)
    print(Y_test.shape)

if __name__ == "__main__":
    main()