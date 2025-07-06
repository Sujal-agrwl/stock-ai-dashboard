# app.py
import streamlit as st
import pandas as pd
from fii_dii_tracker import get_fii_dii_data
from earnings_result import get_results_data
from block_deals import get_block_deals
from gov_news import get_gov_news
from news_fetcher import get_general_news

st.set_page_config(page_title="📊 Stock AI Dashboard", layout="wide")
st.title("📈 Stock Market AI Dashboard")

# --- Section: FII/DII Tracker ---
st.header("📉 FII/DII Tracker")
fii_dii_df = get_fii_dii_data()
if fii_dii_df.empty:
    st.warning("❌ No data fetched.")
else:
    st.success(f"✅ FII/DII Data for: {fii_dii_df.iloc[0]['Date']}")
    st.dataframe(fii_dii_df)

# --- Section: Quarterly Results ---
st.header("📋 Quarterly Earnings Results")
results_df = get_results_data()
if results_df.empty:
    st.info("Markets are closed today (Weekend/Holiday). Quarterly results usually update on working days.")
else:
    st.dataframe(results_df)

# --- Section: Bulk/Block Deals ---
st.header("💼 Bulk & Block Deals")
deals_df = get_block_deals()
if deals_df.empty:
    st.warning("No block or bulk deals found today.")
else:
    st.dataframe(deals_df)

# --- Section: Government & Finance News ---
st.header("📰 Government & Finance Policy News")
gov_df = get_gov_news()
if gov_df.empty:
    st.info("No recent government or finance policy news found.")
else:
    for _, row in gov_df.iterrows():
        st.markdown(f"**{row['title']}**  \n*{row['source']}*  \n{row['description']}")
        st.markdown(f"[Read more]({row['link']})")
        st.divider()

# --- Section: General Business News ---
st.header("🧠 Global & Domestic Market News")
news_df = get_general_news()
if news_df.empty:
    st.info("No business news found.")
else:
    for _, row in news_df.iterrows():
        st.markdown(f"**{row['title']}**  \n*{row['source']}*  \n{row['description']}")
        st.markdown(f"[Read more]({row['link']})")
        st.divider()

st.markdown("---")
st.caption("Made by Sujal Agrawal • Powered by Streamlit & AI")

