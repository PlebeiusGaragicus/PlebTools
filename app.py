import streamlit as st

from enum import Enum


class Pages(Enum):
    # HOME = "🏠 Home"
    # TIMECHAIN = "⏰ :orange[Bitcoin] Timechain"
    # FIAT_CONVERTER = "💸 :green[Fiat] Converter"
    # BTC_HISTORICAL_PRICE = "📈 BTC :blue[Historical] Price"
    HOME = "Home"
    TIMECHAIN = ":orange[Bitcoin Timechain]"
    FIAT_CONVERTER = ":green[Fiat Converter]"
    BTC_HISTORICAL_PRICE = ":blue[BTC Historical Price]"





def home_page():
    st.header(":rainbow[PlebTools]", divider="rainbow")
    st.write("Home page")
    st.markdown(":wave: Welcome!")





def route():
    # if "current_page" not in st.session_state:
    #     st.session_state.current_page = None

    # st.set_page_config(page_title="PlebTools", layout="wide")

    if st.session_state.current_page == Pages.HOME.value:
        home_page()
    elif st.session_state.current_page == Pages.TIMECHAIN.value:
        from tools.timechain import page as timechain_page
        timechain_page()
    elif st.session_state.current_page == Pages.FIAT_CONVERTER.value:
        from tools.fiat_converter import page as fiat_converter_page
        fiat_converter_page()
    else:
        st.error("Page not found")


def on_click(page):
    st.session_state.current_page = page


def show_navigation():
    with st.sidebar:
        for p in Pages:
            button_text = p.value
            if st.session_state.current_page == p.value:
                button_text = f"⭐️ **{button_text}** ⭐️"
            st.button(button_text, on_click=on_click, args=(p.value,), use_container_width=True)












# def show_sidebar():
#     st.sidebar.title("Navigation")
#     st.sidebar.markdown("## 📚 Pages")
#     page = st.sidebar.radio(
#         "Go to",
#         [
#             "Home",
#             "Data Exploration",
#             "Data Cleaning",
#             "Feature Engineering",
#             "Model Training",
#             "Model Evaluation",
#             "Model Interpretation",
#         ],
#     )
#     return page


if __name__ == "__main__":
    # interesting Copilot addition
    # import sys
    # sys.path.append(".")

    if "current_page" not in st.session_state:
        st.session_state.current_page = Pages.HOME.value

    show_navigation()
    route()
