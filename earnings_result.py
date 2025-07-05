# earnings_result.py
import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_results_data():
    url = "https://trendlyne.com/results/latest-results/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        table = soup.find("table", {"class": "table"})

        if not table:
            return pd.DataFrame([])

        data = []
        rows = table.find_all("tr")[1:]  # skip header
        for row in rows[:15]:  # top 15 companies
            cols = row.find_all("td")
            if len(cols) >= 6:
                data.append({
                    "Company": cols[0].get_text(strip=True),
                    "Quarter": cols[1].get_text(strip=True),
                    "Revenue (Cr)": cols[2].get_text(strip=True),
                    "YoY Growth": cols[3].get_text(strip=True),
                    "Net Profit (Cr)": cols[4].get_text(strip=True),
                    "YoY Profit Growth": cols[5].get_text(strip=True)
                })

        return pd.DataFrame(data)

    except Exception as e:
        return pd.DataFrame([])

