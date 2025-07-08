import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredictor():
    #Load the Data
    X=[1,2,3,4,5]
    Y=[3,4,2,4,5]

    print("Values of Independent variables : ",X)
    print("Values of Dependent variables : ",Y)

    mean_x=np.mean(X)
    mean_y=np.mean(Y)

    print("X_MEAN is : ",mean_x)
    print("Y_MEAN is : ",mean_y)

    n=len(X)

    numerator = 0
    denomenator = 0

    #y=mx+c
    for i in range(n):
        numerator=numerator+(X[i]-mean_x)*(Y[i]-mean_y)
        denomenator=denomenator+(X[i]-mean_x)**2

    m=numerator/denomenator
    print("Slope of line  : ",m)

    C=mean_y-(m*mean_x)
    print("Y intercept of line is : ",C)

    Y_predicted=[]
    for i in range(n): 
        Yp = m * X[i] + C
        Y_predicted.append(Yp)
        print("Value of Y predicted is : ",Yp)

    R_numerator = 0
    R_Denomenator = 0
    for i in range (n):
        R_numerator = R_numerator + (Y[i] - Y_predicted[i]) ** 2
        R_Denomenator = R_Denomenator + (Y[i] - mean_y) ** 2

    R_square = 1 - (R_numerator / R_Denomenator)
    print("R² value is : ", R_square)

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()