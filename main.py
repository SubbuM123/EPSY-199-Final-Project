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

class RequestHandler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        #REMOVE
        self.send_header('Access-Control-Allow-Origin', '*')  # Allow requests from any origin
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Decode the received JSON data
        data = json.loads(post_data.decode('utf-8'))

        # Extract input string and chosen color from the data
        input_string = data.get('string', '')
        side = data.get('side', '')

        # Call the main function with the received string and chosen color
        result = main(input_string, side)

        # Send back the result as JSON
        self._set_response()
        self.wfile.write(json.dumps({"result": result}).encode('utf-8'))
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

def main(input_string, side):
    #scrape, pgn to df, df to move analysis, make that a df, then predict
    moves = ScrapeAnalysis(input_string)

    df_usergame = PGNtoDF(moves)

    df_user = pd.DataFrame(columns=["Captures", "Endgame", "Middlegame", "Major Pieces", "Minor Pieces", "Pawn"])

    df_moves = UserGM(df_user, df_usergame, side)

    kmeans = KMeans(n_clusters = 20)
    numeric_columns=[ "Captures" , "Endgame", "Middlegame", "Major Pieces", "Minor Pieces", "Pawn"]

    df = pd.read_csv("games.csv")
    df2 = df.dropna()

    for column in numeric_columns:
        df2[column] = df2[column] / df2[column].abs().max()

    kmeans.fit(df2[numeric_columns])

    cluster = kmeans.predict(df_moves)
    result = cluster[0].astype(str)
    return result

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting server...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()

