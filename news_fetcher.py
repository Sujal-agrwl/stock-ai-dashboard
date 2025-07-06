# news_fetcher.py
import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_general_news():
    try:
        url = "https://economictimes.indiatimes.com/markets"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        news_cards = soup.select(".eachStory")
        data = []

        for card in news_cards[:10]:
            title = card.select_one("h3 a")
            desc = card.select_one(".synopsis")
            link = title.get("href", "") if title else ""
            if title and link:
                data.append({
                    "title": title.text.strip(),
                    "source": "ET Markets",
                    "description": desc.text.strip() if desc else "",
                    "link": "https://economictimes.indiatimes.com" + link if link.startswith("/") else link
                })

        return pd.DataFrame(data)

    except Exception:
        return pd.DataFrame([])

