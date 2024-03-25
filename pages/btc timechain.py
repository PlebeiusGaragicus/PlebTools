import requests

import streamlit as st

# get bitcoin block height from mempool.space
response = requests.get("https://mempool.space/api/blocks/tip/height")
data = response.json()

st.set_page_config(page_title="Bitcoin Block Height", layout="wide")
st.header(f":orange[Bitcoin] block height: :green[{data:,}]", divider="rainbow")

