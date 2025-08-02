from sklearn.metrics import mean_squared_error,r2_score
import numpy as np

def main():
    y_actual = [10,20,30,40,50]
    y_predicted = [12,18,32,38,52]

    print("Actual Values : ",y_actual)
    print("Predicted Values : ",y_predicted)

    MSE = mean_squared_error(y_actual,y_predicted)
    print("Mean squared error : ",MSE)

    RMSE = np.sqrt(MSE)
    print("Root mean squared error : ",RMSE)

if __name__ == "__main__":
    main()
    