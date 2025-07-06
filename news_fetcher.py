# news_fetcher.py
import pandas as pd
from newsapi import NewsApiClient

# Initialize with your NewsAPI key
newsapi = NewsApiClient(api_key='706e8dcdca9b41f7a3200fb62e12c788706e8dcdca9b41f7a3200fb62e12c788')

def get_general_news():
    try:
        response = newsapi.get_everything(
            q="India stock market OR Sensex OR Nifty OR Indian economy OR global market",
            language="en",
            sort_by="publishedAt",
            page_size=10
        )

        articles = response.get("articles", [])
        if not articles:
            return pd.DataFrame([])

        data = []
        for article in articles:
            data.append({
                "title": article.get("title"),
                "source": article.get("source", {}).get("name"),
                "description": article.get("description"),
                "link": article.get("url")
            })

        return pd.DataFrame(data)

    except Exception:
        return pd.DataFrame([])
