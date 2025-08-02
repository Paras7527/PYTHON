from sklearn.metrics import mean_squared_error,r2_score

def main():
    y_actual = [100,200,300,400,500]
    y_predict = [110,190,310,390,510]

    print("Actual Value : ",y_actual)
    print("Predicted Value : ",y_predict)

    R2 = r2_score(y_actual,y_predict)
    print("Value of R square : ",R2)
if __name__ == "__main__":
    main()
    