import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import yfinance as yf
import plotly.graph_objects as go

st.set_page_config(
    page_title="Streamlit Docker",
    layout="wide",
    initial_sidebar_state="collapsed",
)
##st.sidebar.title(":memo: Editor settings")

with st.sidebar:
    selected = option_menu(
        menu_title = "Page Menu",
        options = ["Home","Stock","Fun","DaysofStreamlit"],
        icons = ["house-heart-fill","calendar2-heart-fill","envelope-heart-fill","calendar-day"],
        menu_icon = "menu-app",
        default_index=0,
    )

if selected == "Home":

    display, editor = st.columns((2, 1))


    st.title("Hi from streamlit inside docker")
    st.write("looks like this works properly....WHAT THE ACTUAL FUCK .ddf")
    st.write("What happens if you change the file?")
    st.write("New line? Or another line")
    name = "Slim Shady"
    st.text("My name is {}".format(name))

    st.header("I'm trying a header")

    st.subheader("Subheader")
    st.title("This is a title")

if selected == "Stock":
    st.title("Stock info to come")
    ticker = st.selectbox("Pick Stock Ticker",('^OSEAX','AMZN','AFG.OL','BMA.OL','DNB.OL','EQNR.OL','EPR.OL','GJF.OL','KID.OL','MOWI.OL','PARB.OL','BETS-B.ST'))
    if st.button("Get Price Chart"):
         st.write(ticker)
         stock_data = yf.download(ticker, start = '2020-01-01')
         fig = go.Figure(
             data=[
                 go.Candlestick(
                     x=stock_data.index,
                     open=stock_data["Open"],
                     high=stock_data["High"],
                     low=stock_data["Low"],
                     close=stock_data["Close"],
                )
            ]
        )
         # Customize the historical data graph
         fig.update_layout(xaxis_rangeslider_visible=False)
         # Use the native streamlit theme.
         st.plotly_chart(fig, use_container_width=True)

         st.dataframe(stock_data)
    else:
        st.write("Wopsie")


if selected == "Fun":
    st.write("Having Fun I Hope")


if selected == "DaysofStreamlit":
    st.write("Ny DAG nye muligheter")

    st.header('Day 5: st.write')
    st.write("Hello, simple write :sunglasses:")
    st.write(1234)
    df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
    st.write(df)
    st.write('Below is a DataFrame:', df, 'Above is a dataframe.')