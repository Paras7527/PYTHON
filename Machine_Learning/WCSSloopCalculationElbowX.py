#Unsupervised ML

import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def main(): 
    print("It is the code to Demonstrate the concept of WCSS in k means")

    X = np.array([[1,2],[1,4],[1,0],[1,3],[5,2],[5,6],[5,1],[5,5],[10,2],[10,4],[10,0],[10,3]])

    WCSS = []

    for k in range(1,13):
        model = KMeans(n_clusters=k,init="k-means++",n_init=10,random_state=42)
        model.fit(X)
        print(model.inertia_)   #Intertia keyword works as WCSS
        WCSS.append(model.inertia_)

    plt.plot(range(1,13),WCSS,marker = 'o')
    plt.title("Elbow method for K Means")
    plt.xlabel("Value of k")
    plt.ylabel("Within cluster sum of square")
    plt.grid(True)
    plt.show()
if __name__ == "__main__":
    main()