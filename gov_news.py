# gov_news.py
import pandas as pd
from newsapi import NewsApiClient
import requests
from bs4 import BeautifulSoup

# Initialize NewsAPI client with your API key
newsapi = NewsApiClient(api_key='706e8dcdca9b41f7a3200fb62e12c788706e8dcdca9b41f7a3200fb62e12c788')

def get_gov_news():
    try:
        query = "RBI OR SEBI OR Ministry of Finance OR India economy OR policy"


        response = newsapi.get_everything(
            q=query,
            language="en",
            sort_by="publishedAt",
            page_size=10
        )

        articles = response.get("articles", [])
        if articles:
            data = []
            for article in articles:
                data.append({
                    "title": article.get("title"),
                    "source": article.get("source", {}).get("name"),
                    "description": article.get("description"),
                    "link": article.get("url")
                })
            return pd.DataFrame(data)

        # Fallback to scraping ET Government
        return scrape_fallback_news()

    except Exception:
        return scrape_fallback_news()

def scrape_fallback_news():
    try:
        url = "https://government.economictimes.indiatimes.com/news/economy"
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        cards = soup.select(".eachStory")

        news = []
        for card in cards[:10]:
            title = card.select_one("h3 a")
            desc = card.select_one(".synopsis")
            link = title.get("href") if title else ""
            if title and link:
                news.append({
                    "title": title.text.strip(),
                    "source": "ET Government",
                    "description": desc.text.strip() if desc else "",
                    "link": link
                })

        return pd.DataFrame(news)

    except Exception:
        return pd.DataFrame([])

