"""
src/components/message_display.py
Hiển thị tin nhắn trong chat
"""
import streamlit as st
from src.utils.format import format_timestamp


def render_messages(messages: list):
    """Render tất cả tin nhắn trong conversation"""
    for msg in messages:
        _render_single_message(msg)


def _render_single_message(msg: dict):
    """Render một tin nhắn"""
    role = msg["role"]
    content = msg["content"]
    timestamp = msg.get("timestamp")

    if role == "user":
        _render_user_message(content, timestamp)
    else:
        _render_assistant_message(content, timestamp)


def _render_user_message(content: str, timestamp=None):
    """Render tin nhắn user - bubble bên phải"""
    with st.chat_message("user", avatar="👤"):
        st.markdown(content)
        if timestamp:
            st.markdown(
                f"<span style='font-size:11px;color:var(--text-muted)'>{format_timestamp(timestamp)}</span>",
                unsafe_allow_html=True
            )


def _render_assistant_message(content: str, timestamp=None):
    """Render tin nhắn assistant với avatar sun"""
    with st.chat_message("assistant", avatar="☀️"):
        st.markdown(content)
        if timestamp:
            st.markdown(
                f"<span style='font-size:11px;color:var(--text-muted)'>{format_timestamp(timestamp)}</span>",
                unsafe_allow_html=True
            )


def render_typing_indicator():
    """Hiện animation đang typing"""
    with st.chat_message("assistant", avatar="☀️"):
        st.markdown("""
        <div class="typing-indicator">
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
            <span style="color:var(--text-muted);font-size:13px;margin-left:4px">SunGPT đang trả lời...</span>
        </div>
        """, unsafe_allow_html=True)
