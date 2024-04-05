import streamlit as st

from enum import Enum

from tools.home_page import page as home_page
from tools.timechain import page as timechain_page
from tools.btc_fiat_converter import page as fiat_converter_page
from tools.btc_mining_calcs import page as btc_mining_calcs_page
from tools.btc_historical_price import page as btc_historical_price_page
from tools.nostr_vanity_npub import page as nostr_vanity_npub_page
from tools.nostr_key_converter import page as nostr_key_converter_page
from tools.reader_mode import page as reader_mode_page



class Pages(Enum):
    HOME = ("Home", home_page)

    ### BTC
    TIMECHAIN = (":orange[Bitcoin Timechain]", timechain_page)
    FIAT_CONVERTER = (":green[Fiat Converter]", fiat_converter_page)
    HISTORICAL_PRICE = (":blue[Historical Bitcoin Price]", btc_historical_price_page)
    MINING_CALCS = (":red[Bitcoin Mining Calcs]", btc_mining_calcs_page)

    ### NOSTR
    NOSTR_VANITY_NPUB = (":violet[nostr vanity npub generator]", nostr_vanity_npub_page)
    NOSTR_KEY_CONVERTER = (":violet[nostr key converter]", nostr_key_converter_page)

    ### RSS / WEB
    READER_MODE = (":grey[Reader Mode]", reader_mode_page)




if __name__ == "__main__":
    if "current_page" not in st.session_state:
        st.session_state.current_page = Pages.HOME.value


    def on_click(page):
        st.session_state.current_page = page

    with st.sidebar:
        for p in Pages:
            button_text = p.value[0]
            if st.session_state.current_page == p.value[0]:
                button_text = f"⭐️ **{button_text}** ⭐️"
            st.button(button_text, on_click=on_click, args=(p.value[0],), use_container_width=True)




    for p in Pages:
        if st.session_state.current_page == p.value[0]:
            p.value[1]()
            break
