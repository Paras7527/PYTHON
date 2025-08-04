import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier


def StudentDataset(Datapath):
    Line = 128*"*"
    print(Line)
    df = pd.read_csv(Datapath)
    print("Data Loaded Successfully!!!")
    print(df.head())
    print(Line)

    print("The Total Rows and Column in the Dataset are : ")
    print(df.shape)
    print(Line)

    print("The Overall Description of the dataset is : ")
    print(df.describe())
    print(Line)

    df = df.drop(columns=['G1', 'G2', 'freetime', 'health'])
    print("The Total Rows and Column in the Dataset are : ")
    print(df.shape)
    print(Line)

def main():
    StudentDataset("student-mat.csv")

if __name__ == "__main__":
    main()