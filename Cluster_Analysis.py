import pandas as pd


def main():
    df = pd.read_csv("Labelled_Clusters_Dataset")
    df2 = df[(df["Player"] > 1600) & (df["Player"] <= 1800)]
    df3 = df2.groupby("Cluster").agg("count").reset_index()
    print(df3)

if __name__ == '__main__':
    main()