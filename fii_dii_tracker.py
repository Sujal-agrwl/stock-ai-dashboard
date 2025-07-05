import requests
import pandas as pd
import time

def get_fii_dii_data():
    url = "https://www.nseindia.com/api/fiidiiTradeReact"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "*/*",
        "Referer": "https://www.nseindia.com/"
    }

    try:
        session = requests.Session()
        session.headers.update(headers)
        session.get("https://www.nseindia.com", timeout=10)
        time.sleep(2)
        response = session.get(url, timeout=10)
        data = response.json()

        if isinstance(data, dict) and "data" in data:
            fii_data = data["data"][0]
        elif isinstance(data, list):
            fii_data = data[0]
        else:
            return pd.DataFrame([])

        result = {
            "Date": fii_data.get("date", "N/A"),
            "FII Buy (Cr)": fii_data.get("fiiBuyValue", "N/A"),
            "FII Sell (Cr)": fii_data.get("fiiSellValue", "N/A"),
            "FII Net (Cr)": fii_data.get("fiiNetValue", "N/A"),
            "DII Buy (Cr)": fii_data.get("diiBuyValue", "N/A"),
            "DII Sell (Cr)": fii_data.get("diiSellValue", "N/A"),
            "DII Net (Cr)": fii_data.get("diiNetValue", "N/A"),
        }

        return pd.DataFrame([result])

    except:
        return pd.DataFrame([])
