from bs4 import BeautifulSoup
import requests
import re

def ScrapeAnalysis(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, features="html.parser")
    moves = soup.find('div', class_="pgn").text
    return moves