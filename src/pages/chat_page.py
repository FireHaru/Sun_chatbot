"""
src/pages/chat_page.py
Trang chat chinh - orchestrate tat ca components
"""
import streamlit as st
import os
from src.api.gemini_client import create_model
from src.components.sidebar import render_sidebar
from src.components.welcome import render_welcome
from src.components.message_display import render_messages
from src.components.chat_input import render_chat_input, render_input_footer
from src.components.api_setup import render_api_setup
from src.components.settings import render_settings_content
from src.hooks.use_chat import handle_user_message
from src.lib.session import get_current_conversation, create_conversation


def render_chat_page():
    _auto_init_model()

    # Khoi tao sidebar_open lan dau
    if "sidebar_open" not in st.session_state:
        st.session_state.sidebar_open = True

    # Inject CSS an/hien sidebar + nut toggle
    _inject_sidebar_toggle_css()

    render_sidebar()
    _render_main_content()


def _auto_init_model():
    if not st.session_state.get("api_key_set"):
        api_key = os.getenv("GEMINI_API_KEY", "")
        if api_key:
            model = create_model()
            if model:
                st.session_state.model = model
                st.session_state.api_key_set = True


def _inject_sidebar_toggle_css():
    """An/hien sidebar bang CSS theo session state"""
    sidebar_open = st.session_state.get("sidebar_open", True)
    if not sidebar_open:
        # An sidebar hoan toan nhung HIỂN THỊ nút điều khiển đóng mở gốc
        # va ngan chặn display: none tu stToolbar gay mat nut taskbar
        st.markdown("""
        <style>
        [data-testid="stSidebar"] { display: none !important; }
        [data-testid="stSidebarCollapsedControl"] { 
            display: flex !important; 
            visibility: visible !important;
        }
        [data-testid="stToolbar"] {
            display: flex !important;
        }
        </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <style>
        [data-testid="stSidebar"] { display: flex !important; }
        </style>
        """, unsafe_allow_html=True)


def _render_main_content():
    if not st.session_state.get("api_key_set"):
        _render_header(show_model=False)
        render_api_setup()
        return

    model = st.session_state.get("model")
    if not model:
        st.error("Khong the khoi tao model. Vui long kiem tra API key.")
        return

    _render_header()

    conv = get_current_conversation()
    if conv is None or len(conv["messages"]) == 0:
        render_welcome()
    else:
        render_messages(conv["messages"])

    pending = st.session_state.pop("pending_message", None)
    if pending:
        handle_user_message(pending, model)
        return

    user_input = render_chat_input()
    render_input_footer()

    if user_input:
        with st.chat_message("user", avatar="👤"):
            st.markdown(user_input)
        handle_user_message(user_input, model)


def _render_header(show_model=True):
    """Header voi nut toggle sidebar"""
    sidebar_open = st.session_state.get("sidebar_open", True)

    if not sidebar_open:
        # Sidebar dang dong: hien nut hamburger + title + badge
        col_toggle, col_title, col_badge = st.columns([0.6, 5, 1.5])
        with col_toggle:
            # Bọc div id open_sidebar_btn de dung chung style CSS dep tu styles.py
            st.markdown('<div id="open_sidebar_btn">', unsafe_allow_html=True)
            if st.button("☰", key="open_sidebar_btn_trigger", help="Mo sidebar", use_container_width=True):
                st.session_state.sidebar_open = True
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        with col_title:
            _render_title()
        with col_badge:
            if show_model:
                _render_model_badge()
    else:
        # Sidebar dang mo: chi hien title + badge
        col_title, col_badge = st.columns([5, 1.5])
        with col_title:
            _render_title()
        with col_badge:
            if show_model:
                _render_model_badge()


def _render_title():
    conv = get_current_conversation()
    title = conv["title"] if conv else "SunGPT"
    st.markdown(
        f'<div style="padding:10px 0;font-size:16px;font-weight:600;color:var(--text-primary)">☀️ {title}</div>',
        unsafe_allow_html=True
    )


def _render_model_badge():
    st.markdown(
        '<div style="text-align:right;padding-top:10px"><span class="chat-model-badge">gemini-2.5-flash ⚡</span></div>',
        unsafe_allow_html=True
    )