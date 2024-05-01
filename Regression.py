import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression


def main():
    df = pd.read_csv("Labelled_Clusters_Dataset")
    model = LogisticRegression()


    ind = ["Captures", "Endgame", "Middlegame", "Major Pieces", "Minor Pieces", "Pawn"]
    dep = "Player"

    l = LogisticRegression(random_state=0).fit(df[ind], df[dep])
    print(l.score(df[ind], df[dep]))

    # model.fit(df[ind], df[dep])

    # df["Predictions"] = model.predict(df[ind])
    # df["Residuals"] = df["Player"] - df["Predictions"]
    # df["Error"] = abs(df["Residuals"])

    # err = df["Error"].sum()
    # print(err, err/len(df))

if __name__ == '__main__':
    main()