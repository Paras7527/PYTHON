import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib

def Titanic(Datapath):
    df = pd.read_csv(Datapath)
    df.drop(columns = ['Passengerid','zero'], inplace=True)
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

    x = df.drop(columns=['Survived'])
    y = df['Survived']

    scaler = StandardScaler()
    x_scale = scaler.fit_transform(x)

    x_train, x_test, y_train, y_test = train_test_split(x_scale, y, test_size=0.2, random_state=42)

    model = LogisticRegression()
    model.fit(x_train, y_train)

    # Save model and scaler
    joblib.dump(model, 'model/titanic_model.pkl')
    joblib.dump(scaler, 'model/scaler.pkl')

    print("Model and Scaler saved successfully!")

if __name__ == "__main__":
    Titanic("MarvellousTitanicDataset.csv")
