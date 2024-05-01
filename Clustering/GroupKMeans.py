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

    kmeans = KMeans(n_clusters = 20)
    numeric_columns=[ "Captures" , "Endgame", "Middlegame", "Major Pieces", "Minor Pieces", "Pawn"]

    df = pd.read_csv("ToCluster")
    df2 = df.dropna()

    for column in numeric_columns:
        df2[column] = df2[column] / df2[column].abs().max()

    kmeans.fit(df2[numeric_columns])

    centers = kmeans.cluster_centers_

    data = []
    for i in centers:
        data.append(i)

    df_centers = pd.DataFrame(data, columns=["Captures", "Endgame", "Middlegame", "Major Pieces", "Minor Pieces", "Pawn"])
    
    variance = []
    for j in numeric_columns:
        variance.append(df_centers[j])
        
    kmeans.predict(df2.iloc[1])

    df_labeled = df2
    df_labeled["Cluster"] = kmeans.labels_

    path = "C:\Projects\EPSY-199-Final-Project/KMeansData/Labelled_Clusters_Dataset"
    df_labeled.to_csv(path, encoding='utf-8', index=False)



if __name__ == '__main__':
    main()

