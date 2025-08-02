import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("iris.csv")

    X = df.iloc[:,[0,1,2,3]].values

    WCSS = []

    for k in range(1,11):
        model = KMeans(n_clusters=k,init="k-means++",n_init=10,random_state=42)
        model.fit(X)
        print(model.inertia_)   #Intertia keyword works as WCSS
        WCSS.append(model.inertia_)

    plt.plot(range(1,11),WCSS,marker = 'o')
    plt.title("Elbow method for K Means")
    plt.xlabel("Value of k")
    plt.ylabel("Within cluster sum of square")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()