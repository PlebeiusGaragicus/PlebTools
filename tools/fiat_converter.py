import requests
import time
import json
import pandas as pd

import streamlit as st



def btc_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    response = requests.get(url)
    data = response.json()
    return data["bpi"]["USD"]["rate"]

def btc_to_fiat(sats: float, price: float) -> float:
    return sats * price / 100_000_000

def fiat_to_btc(fiat: float, price: float) -> float:
    return int(fiat / price * 100_000_000)


def page():

    coinbase_price = btc_price()
    bitcoin_price = coinbase_price.replace(",", "")
    bitcoin_price = float(bitcoin_price)

    p = bitcoin_price

    # st.set_page_config(page_title="Bitcoin, Fiat Converter", layout="wide")
    st.header(":orange[bitcoin] to :green[fiat] converter", divider="rainbow")
    st.markdown(f"# Bitcoin price: :orange[${coinbase_price}]")



    with st.container(border=True):
        cols2 = st.columns(2)
        with cols2[0]:
            # st.write("Bitcoin to Fiat")
            st.write(f"1 sat = ${btc_to_fiat(1, price=bitcoin_price):,.2f} fiat")
            st.write(f"1,000 sats = ${btc_to_fiat(1_000, price=bitcoin_price):,.2f} fiat")
        
        with cols2[1]:
            # st.write("Fiat to Bitcoin")
            st.write(f"$1 = {fiat_to_btc(1, price=bitcoin_price)} sats")
            st.write(f"$100 = {fiat_to_btc(100, price=bitcoin_price)} sats")
            st.write(f"$1000 = {fiat_to_btc(1000, price=bitcoin_price)} sats")


    col2 = st.columns(2)
    with col2[0].form(key="btc_fiat", border=False):
        st.markdown(":orange[Bitcoin to Fiat]")
        sats = st.number_input("satoshi", min_value=0.0, step=1.0, format="%f")
        # %d %e %f %g %i %u

        if st.form_submit_button("Convert"):
            fiat = sats * p / 100_000_000
            st.write(f"fiat: :green[${fiat:,.2f}]")


    with col2[1].form("fiat_btc", border=False):
        st.markdown(":green[Fiat to Bitcoin]")
        fiat = st.number_input("fiats", min_value=0.0, step=0.01, format="%f")

        if st.form_submit_button("Convert"):
            btc = fiat / p * 100_000_000
            st.write(f"satoshi: :orange[{btc:,.0f}]")
            if btc > 100_000_000:
                # st.write("You need more money to buy bitcoin")
                st.write(f"btc: :orange[{btc / 100_000_000:,.4f}]")
