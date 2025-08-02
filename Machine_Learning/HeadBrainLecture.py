import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error

def MarvellousHeadBrainLinear(Datapath):
    Line = "*"*80
    df = pd.read_csv(Datapath)

    print(Line)
    print("First few records of the datasets are :")
    print(Line)
    print(df.head())
    print(Line)

    print("Statistical info of the datasets : ")
    print(Line)
    print(df.describe())
    print(Line)

    x = df[['Head Size(cm^3)']]
    y = df[['Brain Weight(grams)']]

    print("Independent Variables are : Head Size")
    print("Dependent Variables are : Brain Weight")
    print("Total records in dataset : ",x.shape)
    print(Line)

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

    print("Dimensions of training dataset : ",x_train.shape)
    print("Dimensions of testing dataset : ",x_test.shape)
    print(Line)

    model = LinearRegression()
    model.fit(x_train,y_train)

    y_predict = model.predict(x_test)

    mse = mean_squared_error(y_test,y_predict)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test,y_predict)

    print("Mean squared error : ",mse)
    print("Root mean square : ",rmse)
    print("R square value : ",r2)
    print(Line)

def main():
    MarvellousHeadBrainLinear("HeadBrain.csv")

if __name__ == "__main__":
    main()
    