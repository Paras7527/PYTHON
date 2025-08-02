import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split

def MarvellousAdvertise(Datapath):
    Line = "*"*80

    df = pd.read_csv(Datapath)
    print(Line)
    print("Data set : ")
    print(df.head())

    print("Clean the dataset : ")
    df.drop(columns = ["Unnamed: 0"],inplace = True)    # to remove

    print(Line)
    print("Updated dataset is : ")
    print(df.head())

    print(Line)
    print("Missing values in each column :",df.isnull().sum())

    print(Line)
    print("Statistical Summary : \n",df.describe())

    print(Line)
    print("Corelation Matrix : ")
    print(df.corr())

    print(Line)
    print("Heat Map : ")
    plt.figure(figsize=(10,5))
    sns.heatmap(df.corr(),annot=True,cmap='coolwarm')
    plt.title("Marvellous Corelation Heat Map")
    plt.show()

    print(Line)
    print("Pairplot : ")
    sns.pairplot(df)
    plt.suptitle("Pairplot of Features",y=1.02)
    plt.show()

    x = df[['TV','radio','newspaper']]
    y = df['sales']

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

    model = LinearRegression()

    model.fit(x_train,y_train)

    y_predict = model.predict(x_test)

    print(Line)
    MSE = metrics.mean_squared_error(y_test,y_predict)
    print("Mean squared error : ",MSE)

    RMSE = np.sqrt(MSE)
    print("Root mean square error : ",RMSE)

    R2 = metrics.r2_score(y_test,y_predict)
    print("value of R square : ",R2)

    print("Model coefficient are : ")
    for col,coef in zip(x.columns,model.coef_):
        print(f"{col} : {coef}")
        print("Y intercept is : ",model.intercept_)

    plt.figure(figsize=(8,5))
    plt.scatter(y_test,y_predict,color = 'blue')
    plt.xlabel("Actual sales : ")
    plt.ylabel("Predicted sales :")
    plt.title("Marvellous Advertisement")
    plt.grid()
    plt.show()

    print(Line)
def main():
    MarvellousAdvertise("Advertising.csv")
if __name__ == "__main__":
    main()