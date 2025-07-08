from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

def main():
    df=pd.read_csv("iris.csv")

    sns.pairplot(df,hue="variety")

    plt.show()

if __name__ == "__main__":
    main()