import pandas as pd
from sklearn.model_selection import train_test_split

def Load_Data(file_path):
    df=pd.read_csv(file_path)
    print("Data Loaded Successfuly !!!")
    return df

def Get_Info(df):
    print("The Info of the Loaded data is :")
    print("Shape of Data set is : ",df.shape)
    print("Columns are : ",df.columns)
    print("Missing Values : ",df.isnull().sum())

def Encode_Data(df):
    df["variety"]=df["variety"].map({"Setosa":1,"Versicolor":2,"Virginica":3})
    return df

def Split_Data(df):
    X=df.drop("variety",axis=1)
    Y=df["variety"]
    return X,Y

def Split(X,Y,size=0.2):
    return train_test_split(X,Y,test_size=size)

def Train():
    pass

def main():
    Data=Load_Data("iris.csv")
    print(Data.head())

    Get_Info(Data)

    print("Data after encoding : ")
    Data=Encode_Data(Data)
    print(Data.head())

    Independent,Dependent=Split_Data(Data)
    print("The Independent Data is :")
    print(Independent.head())
    print("The Depenedent Data is :")
    print(Dependent.head())

    X_train,X_test,Y_train,Y_test=Split(Independent,Dependent,size=0.3)
    print(X_train.shape)
    print(X_test.shape)
    print(Y_train.shape)
    print(Y_test.shape)



if __name__=="__main__":
    main()