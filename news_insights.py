# news_insights.py
import pandas as pd

impact_rules = [
    {
        "keywords": ["EV", "electric vehicle", "GST"],
        "stocks": ["Tata Motors", "Ashok Leyland", "Olectra Greentech"],
        "sector": "Electric Vehicles",
        "direction": "Negative"
    },
    {
        "keywords": ["solar", "renewable", "green energy"],
        "stocks": ["Tata Power", "Adani Green", "JSW Energy"],
        "sector": "Renewable Energy",
        "direction": "Positive"
    },
    {
        "keywords": ["repo rate", "RBI hike", "interest rate"],
        "stocks": ["Banks", "NBFCs"],
        "sector": "Banking",
        "direction": "Negative"
    },
    {
        "keywords": ["HDFC Bank", "ICICI Bank", "SBI profit"],
        "stocks": ["HDFC Bank"],
        "sector": "Banking",
        "direction": "Positive"
    },
    {
        "keywords": ["SEBI", "IPO", "listing"],
        "stocks": ["SME IPOs", "Angel One", "Zerodha"],
        "sector": "Capital Markets",
        "direction": "Positive"
    },
    {
        "keywords": ["smartphone", "import duty", "mobile phone"],
        "stocks": ["Apple suppliers", "Micromax", "Dixon Tech"],
        "sector": "Consumer Electronics",
        "direction": "Negative"
    }
]

def analyze_headlines(headlines):
    insights = []
    for headline in headlines:
        matched = False
        for rule in impact_rules:
            if any(k.lower() in headline.lower() for k in rule["keywords"]):
                insights.append({
                    "News": headline,
                    "Sector": rule["sector"],
                    "Impact": rule["direction"],
                    "Likely Affected Stocks": ", ".join(rule["stocks"])
                })
                matched = True
                break
        if not matched:
            insights.append({
                "News": headline,
                "Sector": "Unclassified",
                "Impact": "Neutral",
                "Likely Affected Stocks": "N/A"
            })
    return pd.DataFrame(insights)