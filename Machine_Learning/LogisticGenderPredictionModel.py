import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

def MarvellousLogistic(datasetpath):
    df = pd.read_csv(datasetpath)           #Data Loading
    print("Dimension of dataframe",df.shape)

    print("Initial data is : ")             #Data printing
    print(df.head())

    df['Gender'] = df['Gender'].map({'Male' : 1 , 'Female' : 0})    #Data Encoding
    print("Encoded data is : ")             
    print(df.head())
    
    #Scatter Plot 
    plt.figure(figsize=(8,6))   #Size is in inch
    sns.scatterplot(data=df, x='Height', y='Weight', hue='Gender', palette='Set1')
    plt.title("Marvellous Weight Height Predictor")
    plt.xlabel("Height")
    plt.ylabel("Weight")
    plt.grid(True)
    plt.show()

    X = df[['Height','Weight']]     #Splitting
    Y = df['Gender']

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    model = LogisticRegression()
    
    model.fit(X_train,Y_train)

    Y_Predict = model.predict(X_test)

    accuracy = accuracy_score(Y_test,Y_Predict)
    print("Accuracy Score is : ",accuracy*100)

    Conf_Matrix = confusion_matrix(Y_test,Y_Predict)
    print("Confusion matrix is :")
    print(Conf_Matrix)

    report = classification_report(Y_test,Y_Predict)
    print("Classification report is :")
    print(report)

def main():
    MarvellousLogistic("weight-height.csv")

if __name__ == "__main__":
    main()

#Accuracy Score is :  92.45
#Confusion matrix is :
#[[903  85]
# [ 66 946]]