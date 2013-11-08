from bs4 import BeautifulSoup

def extract_contributions(html):
    soup = BeautifulSoup(html)
    svg = soup.find("svg", id = "calendar-graph")

