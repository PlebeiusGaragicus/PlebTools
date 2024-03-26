import requests
import streamlit as st
import re

# haven't used this yet - https://github.com/zyocum/reader
# NOTE: we are using this - https://github.com/alan-turing-institute/ReadabiliPy
from readabilipy import simple_json_from_html_string

st.set_page_config(page_title="Website reader mode", layout="wide")
st.header(":grey[Website reader mode]", divider="rainbow")

st.caption("https://tftc.io/home-and-car-insurance-providers-retreating/")

# url = st.text_input("Enter URL")

if url := st.text_input("Enter URL"):
    req = requests.get( url )
    article = simple_json_from_html_string(req.text, use_readability=True)


    st.header(article["title"])
    st.caption(f"by: {article['byline']}")
    if article['date'] is not None:
        st.caption(article["date"])
    else:
        st.caption("No date found")

    # NoneType errors... forget this way
    # byline_date = article.get("byline", "")
    # if article.get("date") is not None:
    #     byline_date += " | " + article["date"]
    # st.caption(byline_date)

    content = article["content"]

    # remove leading spaces after newlines that appears before a tag
    content = re.sub("\n\s+", "\n", content)


    st.markdown(content, unsafe_allow_html=True)
    with st.expander("Show JSON"):
        st.write(article)
