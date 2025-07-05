# app.py
import streamlit as st
import pandas as pd
from fii_dii_tracker import get_fii_dii_data
from news_fetcher import get_news_data
from earnings_result import get_results_data
from block_deals import get_block_deals

st.set_page_config(page_title="Stock AI Dashboard", layout="wide")
st.title("📊 Stock AI Dashboard – India")

# --- FII/DII Tracker ---
st.header("FII/DII Activity")
fii_dii_df = get_fii_dii_data()
if fii_dii_df.empty:
    st.warning("No FII/DII data available. Try again later.")
else:
    st.dataframe(fii_dii_df)

# --- News Fetcher ---
st.header("📢 Market News & Sentiment")
news_df = get_news_data()
if news_df.empty:
    st.warning("No news available.")
else:
    for idx, row in news_df.iterrows():
        st.markdown(f"**{row['title']}**")
        st.caption(row['source'])
        st.write(row['summary'])
        st.markdown(f"[Read more]({row['link']})")
        st.divider()

# --- Earnings Results ---
st.header("📈 Quarterly Results")
results_df = get_results_data()
if results_df.empty:
    st.warning("No result data fetched.")
else:
    st.dataframe(results_df)

# --- Block/Bulk Deals ---
st.header("📦 Bulk & Block Deals")
deals_df = get_block_deals()
if deals_df.empty:
    st.warning("No deal data found today.")
else:
    st.dataframe(deals_df)

st.markdown("---")
st.caption("Built by Sujal with ChatGPT 💡")

