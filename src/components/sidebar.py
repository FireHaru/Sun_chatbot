"""
src/components/sidebar.py
Sidebar component: logo, new chat, conversation list, toggle button
"""
import streamlit as st
from src.lib.session import (
    create_conversation, get_all_conversations,
    switch_conversation, delete_conversation
)
from src.components.settings import render_settings_content
from src.utils.format import truncate_text


def render_sidebar():
    """Render toàn bộ sidebar"""
    with st.sidebar:
        _render_logo()
        _render_new_chat_btn()

        st.markdown("<hr style='margin:8px 0'>", unsafe_allow_html=True)

        # Search
        _render_search()

        # Settings dưới search
        render_settings_content()

        st.markdown("<hr style='margin:8px 0'>", unsafe_allow_html=True)

        # Conversations
        _render_conversation_list()

        # Footer cố định đáy
        _render_sidebar_footer()


def _render_logo():
    """Logo SunGPT"""
    st.markdown("""
    <div class="sungpt-logo">
        <span class="sungpt-logo-icon">☀️</span>
        <span class="sungpt-logo-text">SunGPT</span>
    </div>
    """, unsafe_allow_html=True)


def _render_new_chat_btn():
    if st.button("✏️  Cuộc trò chuyện mới", use_container_width=True, key="new_chat_btn"):
        create_conversation()
        st.rerun()


def _render_search():
    search = st.text_input(
        "search",
        placeholder="🔍 Tìm kiếm...",
        label_visibility="collapsed",
        key="search_query_input"
    )
    st.session_state.search_query = search


def _render_conversation_list():
    conversations = get_all_conversations()
    search_q = st.session_state.get("search_query", "").lower()

    if search_q:
        conversations = [
            (cid, conv) for cid, conv in conversations
            if search_q in conv["title"].lower()
        ]

    if not conversations:
        if search_q:
            st.markdown(
                "<p style='color:var(--text-muted);font-size:12px;padding:8px 16px'>Không tìm thấy</p>",
                unsafe_allow_html=True
            )
        return

    st.markdown("<div class='conv-section-title'>Lịch sử</div>", unsafe_allow_html=True)

    current_id = st.session_state.current_conv_id

    for conv_id, conv in conversations:
        is_active = conv_id == current_id
        title = truncate_text(conv["title"], 35)
        col1, col2 = st.columns([5, 1])
        with col1:
            if st.button(
                f"💬 {title}",
                key=f"conv_{conv_id}",
                use_container_width=True,
                type="primary" if is_active else "secondary",
            ):
                switch_conversation(conv_id)
                st.rerun()
        with col2:
            if st.button("🗑", key=f"del_{conv_id}", help="Xóa cuộc trò chuyện"):
                delete_conversation(conv_id)
                st.rerun()


def _render_sidebar_footer():
    st.markdown("""
    <div class="sidebar-footer">
        ☀️ SunGPT — Trợ lý học code
    </div>
    """, unsafe_allow_html=True)
