# Goal
# Fetch a webpage using requests
# Parse HTML using BeautifulSoup
# Extract specific information (e.g., news headlines, weather, exchange rates)

import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

print("📰 Naver Main News Headlines:")

# Get news headlines
for idx, headline in enumerate(soup.select(".hdline_article_tit a"), 1):
    print(f"{idx}. {headline.text.strip()}")
