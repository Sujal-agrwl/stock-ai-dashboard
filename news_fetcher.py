import pandas as pd

def get_news_data():
    data = [
        {
            "title": "Sensex rallies 400 points",
            "summary": "Markets closed higher today as IT and banking stocks gained.",
            "source": "Moneycontrol",
            "link": "https://www.moneycontrol.com"
        },
        {
            "title": "RBI policy preview",
            "summary": "Experts expect no rate change in upcoming monetary policy.",
            "source": "Economic Times",
            "link": "https://economictimes.indiatimes.com"
        }
    ]
    return pd.DataFrame(data)
