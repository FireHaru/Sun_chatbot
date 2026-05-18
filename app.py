cd """
SunGPT - Trợ lý AI chuyên dạy code
Entry point chính của ứng dụng
"""
import streamlit as st
from src.lib.session import init_session
from src.pages.chat_page import render_chat_page
from src.lib.styles import inject_styles

def main():
    st.set_page_config(
        page_title="SunGPT — Trợ lý học code",
        page_icon="☀️",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_styles()
    init_session()
    if "sidebar_open" not in st.session_state:
        st.session_state.sidebar_open = True
    render_chat_page()

if __name__ == "__main__":
    main()
