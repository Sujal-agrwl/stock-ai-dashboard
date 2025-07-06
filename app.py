import streamlit as st
import pandas as pd
from news_fetcher import get_general_news
from gov_news import get_gov_news
from news_insights import analyze_headlines

st.set_page_config(page_title="📊 Stock AI Dashboard", layout="wide")
st.title("🧠 Stock AI News Impact Dashboard")

# ✅ Government News Section
st.header("📰 Government & Finance Policy News")
gov_news_df = get_gov_news()

st.subheader("🛠 Debug: Raw Government News")
st.write(gov_news_df)

if not gov_news_df.empty and "title" in gov_news_df.columns:
    st.dataframe(gov_news_df[["title", "source", "link"]])
    st.subheader("📌 News Impact Insights (Gov News)")
    insights = analyze_headlines(gov_news_df["title"].tolist())
    st.dataframe(insights)
else:
    st.info("No recent government or finance policy news found.")

# ✅ General Business News Section
st.header("📈 Global & Domestic Market News")
gen_news_df = get_general_news()

st.subheader("🛠 Debug: Raw Business News")
st.write(gen_news_df)

if not gen_news_df.empty and "title" in gen_news_df.columns:
    st.dataframe(gen_news_df[["title", "source", "link"]])
    st.subheader("📌 News Impact Insights (General News)")
    insights = analyze_headlines(gen_news_df["title"].tolist())
    st.dataframe(insights)
else:
    st.info("No business news found.")


