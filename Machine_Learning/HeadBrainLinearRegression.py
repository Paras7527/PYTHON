#HEAD SIZE = BRAIN SIZE
#LOGISTIC REGRESSION

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

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

    X = df[["Head Size(cm^3)"]]
    Y = df["Brain Weight(grams)"]

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.4,random_state=42)

    model = LinearRegression()

    model.fit(X_train,Y_train)

    Y_predict = model.predict(X_test)
    print(Y_predict)

    mae = mean_absolute_error(Y_test, Y_predict)
    mse = mean_squared_error(Y_test, Y_predict)
    r2 = r2_score(Y_test, Y_predict)

    print(f"\nEvaluation Metrics:")
    print(f"Mean Absolute Error (MAE): {mae:.2f}")
    print(f"Mean Squared Error (MSE): {mse:.2f}")
    print(f"R² Score: {r2:.2f}")

def main():
    HeadBrainModel("HeadBrain.csv")

if __name__ == "__main__":
    main()