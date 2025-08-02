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
    
    model = KMeans(n_clusters=3,init='k-means++',n_init=10,random_state=42)
    y_kmeans = model.fit_predict(X)

    plt.scatter(X[y_kmeans == 0,0],X[y_kmeans == 0,1],s=100,c='orange',label = 'Setosa')

    plt.scatter(X[y_kmeans == 1,0],X[y_kmeans == 1,1],s=100,c='green',label = 'Versicolor')

    plt.scatter(X[y_kmeans == 2,0],X[y_kmeans == 2,1],s=100,c='blue',label = 'Virginica')

    plt.scatter(model.cluster_centers_[:,0],model.cluster_centers_[:,1],s=100,c='lightblue',label = 'centroid')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()