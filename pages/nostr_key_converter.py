from nostr_protocol import Keys

import streamlit as st

st.set_page_config(page_title="Nostr Key Converter", layout="wide")
st.header(f":violet[nostr] key converter", divider="rainbow")

st.caption("Convert between hex and bech32 keys :red[/] see also: https://nostrtool.com/")

# cols2 = st.columns((3, 1))
cols2 = st.columns((1, 4))

with cols2[0]:
    st.radio("key is a", [":green[public] key", ":red[secret] key", ":blue[mnemonic]"], key="key_type")


with cols2[1]:
    input = st.text_input("key material")

    mnemonic = ""
    if st.session_state.key_type == ":blue[mnemonic]":
        mnemonic = st.text_input("passphrase")

col2 = st.columns(2)

if input:
    if st.session_state.key_type == ":blue[mnemonic]":
        key = Keys.from_mnemonic(input, passphrase=mnemonic)
    else:
        key = Keys.parse(input)

    if st.session_state.key_type != ":red[secret] key":
        with col2[0]:
            with st.container(border=True):
                st.write(":green[Public key]:")
                st.write(f"     hex:    `{key.public_key().to_hex()}`")
                st.write(f"     bech32: `{key.public_key().to_bech32()}`")

    with col2[1]:
        with st.container(border=True):
            st.write(":red[Secret key]:")
            st.write(f"     hex:    `{key.secret_key().to_hex()}`")
            st.write(f"     bech32: `{key.secret_key().to_bech32()}`")
