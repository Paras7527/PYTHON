import numpy as np
from sklearn.cluster import KMeans

def main(): 
    print("It is the code to Demonstrate the concept of WCSS in k means")

    X = np.array([[1,2],[1,4],[1,0],[1,3],[10,2],[10,4],[10,0],[10,3]])

    for k in range(1,9):
        model = KMeans(n_clusters=k,init="k-means++",n_init=10,random_state=42)
        model.fit(X)
        print(model.inertia_)   #Intertia keyword works as WCSS

if __name__ == "__main__":
    main()