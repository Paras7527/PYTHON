import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

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



def main():
    MarvellousLogistic("weight-height.csv")

if __name__ == "__main__":
    main()