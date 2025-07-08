import pandas as pd
import matplotlib.pyplot as plt

def main():
    data={'X':[2,4,6,8,10],'Y':[1,3,5,7,9]}

    df=pd.DataFrame(data)
    df.plot(x='X',y='Y',kind='bar')
    plt.title("Graph")
    plt.show()

if __name__=="__main__":
    main()

