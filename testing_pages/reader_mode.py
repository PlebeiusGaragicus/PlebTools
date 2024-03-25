import streamlit as st

import requests
from readability import Document

st.header(":grey[Website reader mode]", divider="rainbow")


st.caption("https://tftc.io/home-and-car-insurance-providers-retreating/")

url = st.text_input("Enter URL")

if url:
    # url = "https://tftc.io/home-and-car-insurance-providers-retreating/"
    response = requests.get( url )

    if response.status_code != 200:
        st.write("URL not found")
        st.stop()

    doc = Document(response.content)

    # doc.title()
    # doc.summary()
    # doc.content()

    st.markdown(f"# {doc.title()}")
    st.write(doc.summary(), unsafe_allow_html=True)
    # st.write()
    # st.write(doc.content())