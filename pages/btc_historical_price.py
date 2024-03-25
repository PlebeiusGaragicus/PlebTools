import requests
import time
import pandas as pd

import streamlit as st



def btc_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    response = requests.get(url)
    data = response.json()
    return data["bpi"]["USD"]["rate"]


def coinbase_fetch_price_history(start_timestamp: int, end_timestamp: int) -> pd.DataFrame:
    """
        refer to: https://docs.cloud.coinbase.com/exchange/reference/exchangerestapi_getproductcandles
        code example taken from: https://www.cryptodatadownload.com/blog/posts/Use-Python-to-Download-Coinbase-Price-Data/
    """
    SYMBOL = 'BTC-USD'
    import http.client
    import json

    conn = http.client.HTTPSConnection("api.exchange.coinbase.com")
    payload = ''
    headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'My App'
    }
    conn.request("GET", "/products/BTC-USD/candles", payload, headers)
    res = conn.getresponse()
    data = res.read()
    # print(data.decode("utf-8"))
    data = json.loads(data.decode("utf-8"))
    # df = pd.DataFrame(data, columns=['unix', 'low', 'high', 'open', 'close', 'volume'])
    df = pd.DataFrame(data, columns=['unix', 'low', 'high', 'open', 'close', 'volume'])
    df['date'] = pd.to_datetime(df['unix'], unit='s')  # convert to a readable date
    df.drop(columns=['volume'], inplace=True)
    df.drop(columns=['open'], inplace=True)
    df.drop(columns=['close'], inplace=True)
    return df



coinbase_price = btc_price()
bitcoin_price = coinbase_price.replace(",", "")
bitcoin_price = float(bitcoin_price)

p = bitcoin_price



st.set_page_config(page_title="Bitcoin Historical Price", layout="wide")
st.header(":orange[bitcoin] :green[historical price]", divider="rainbow")
st.markdown(f"# Bitcoin price: :orange[${coinbase_price}]")


# graph historical price
ninety_days_ago = time.time() - (90 * 24 * 60 * 60)
with st.spinner("Loading data..."):
    historical_price = coinbase_fetch_price_history(ninety_days_ago, time.time())
st.line_chart(historical_price, y=["high", "low"], x="date")
