import pandas as pd
from bs4 import BeautifulSoup
import requests
import re
from sklearn.cluster import KMeans
import numpy as np
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from scrape import ScrapeAnalysis
from format import PGNtoDF
from game_analysis import UserGM

def main():
    #scrape, pgn to df, df to move analysis, make that a df, then predict

    AllSTD = []
    AllMean = []
    for i in range(1000, 2400, 200):

        kmeans = KMeans(n_clusters = 5)
        numeric_columns=[ "Captures" , "Endgame", "Middlegame", "Major Pieces", "Minor Pieces", "Pawn"]

        df = pd.read_csv("KMeansData/" + str(i) + "-" + str(i + 200))
        df2 = df.dropna()

        for column in numeric_columns:
            df2[column] = df2[column] / df2[column].abs().max()

        kmeans.fit(df2[numeric_columns])

        centers = kmeans.cluster_centers_

        
        data = []
        for i in centers:
            data.append(i)

        df_centers = pd.DataFrame(data, columns=["Captures", "Endgame", "Middlegame", "Major Pieces", "Minor Pieces", "Pawn"])
        
        std = []
        mean = []
        for j in numeric_columns:
            std.append(df_centers[j].std())
            mean.append(df_centers[j].mean())
        
        AllSTD.append(std)
        AllMean.append(mean)

        
    df_std = pd.DataFrame(AllSTD, columns=["Captures", "Endgame", "Middlegame", "Major Pieces", "Minor Pieces", "Pawn"])
    df_mean = pd.DataFrame(AllMean, columns=["Captures", "Endgame", "Middlegame", "Major Pieces", "Minor Pieces", "Pawn"])
    
    path = "C:\Projects\EPSY-199-Final-Project/JupyterData"
    df_std.to_csv(path + "/STD.csv", encoding='utf-8', index=False)
    df_mean.to_csv(path + "/Mean.csv", encoding='utf-8', index=False)
    # cluster = kmeans.predict(df_moves)
    # result = cluster[0].astype(str)
    # return result

if __name__ == '__main__':
    main()