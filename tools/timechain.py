import requests

import streamlit as st

def page():
    # https://blockstream.info/api/blocks/tip/height
    # get bitcoin block height from mempool.space
    st.header(f":orange[Bitcoin] block height", divider="rainbow")

    response = requests.get("https://mempool.space/api/blocks/tip/height")
    data = response.json()

    # st.set_page_config(page_title="Bitcoin Block Height", layout="wide")

    st.header(f":green[{data:,}]")
