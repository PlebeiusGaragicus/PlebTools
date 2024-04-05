import streamlit as st

from nostr_protocol import Keys

def page():

    # st.set_page_config(page_title="nostr vanity npub generator", layout="wide")
    st.header(f":violet[nostr] vanity npub generator", divider="rainbow")

    st.caption("warning: 6 letters or longer may take a :blue[***long time***] to generate")

    if prefix := st.text_input("Prefix"):
        with st.spinner("Mining keys..."):
            keys = Keys.vanity([prefix], True, 8)

            sk = keys.secret_key()
            pk = keys.public_key()
            st.write(":green[Public keys]:")
            st.write(f"     hex:    `{pk.to_hex()}`")
            st.write(f"     bech32: `{pk.to_bech32()}`")
            st.write(":red[Secret keys]:")
            st.write(f"     hex:    `{sk.to_hex()}`")
            st.write(f"     bech32: `{sk.to_bech32()}`")
