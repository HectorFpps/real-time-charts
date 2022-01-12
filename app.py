import streamlit as st
import yfinance
import pandas as pd
import pandas_ta as ta

ticker = str(st.text_input("-Input Desired Ticker (Yahoo Finance)"))

while True:
    df = pd.DataFrame()
    df = df.ta.ticker(ticker, period="100d", interval="1h")
    st.line_chart(df.Close)

