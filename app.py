import streamlit as st
import pandas as pd
from news_fetcher import get_general_news
from gov_news import get_gov_news
from news_insights import analyze_headlines

st.set_page_config(page_title="📊 Stock AI Dashboard", layout="wide")
st.title("🧠 Stock AI News Impact Dashboard")

# Government News
st.header("📰 Government & Finance Policy News")
gov_news_df = get_gov_news()
if not gov_news_df.empty:
    st.dataframe(gov_news_df[["title", "source", "link"]])
    st.subheader("📌 News Impact Insights (Gov News)")
    gov_insights = analyze_headlines(gov_news_df["title"].tolist())
    st.dataframe(gov_insights)
else:
    st.info("No recent government or finance policy news found.")

# Business News
st.header("📈 Global & Domestic Market News")
gen_news_df = get_general_news()
if not gen_news_df.empty:
    st.dataframe(gen_news_df[["title", "source", "link"]])
    st.subheader("📌 News Impact Insights (General News)")
    gen_insights = analyze_headlines(gen_news_df["title"].tolist())
    st.dataframe(gen_insights)
else:
    st.info("No business news found.")

