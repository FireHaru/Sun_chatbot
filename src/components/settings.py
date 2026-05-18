"""
src/components/settings.py
Panel cài đặt sidebar
"""
import streamlit as st
import os
from src.api.gemini_client import create_model


def render_settings_content():
    """Render settings content trong sidebar"""
    with st.expander("⚙️ Cài đặt", expanded=False):
            st.markdown("**API Key**")

            new_key = st.text_input(
                "Gemini API Key",
                type="password",
                value="",
                placeholder="Nhập API key mới...",
                label_visibility="collapsed",
            )

            if st.button("💾 Lưu", use_container_width=True):
                if new_key:
                    os.environ["GEMINI_API_KEY"] = new_key
                    model = create_model()
                    if model:
                        st.session_state.model = model
                        st.session_state.api_key_set = True
                        st.success("✅ Đã cập nhật!")
                        st.rerun()
                    else:
                        st.error("❌ Key không hợp lệ")

            st.markdown("---")
            st.markdown("**Model**: `gemini-2.5-flash`")
            st.markdown("**Phiên bản**: `1.0.0`")
            st.markdown("**Theme**: Dark Mode")

            # Clear all conversations
            st.markdown("---")
            if st.button("🗑️ Xóa tất cả cuộc trò chuyện", use_container_width=True):
                st.session_state.conversations = {}
                st.session_state.current_conv_id = None
                st.success("Đã xóa tất cả!")
                st.rerun()
# Backward compatibility với code cũ
render_settings_sidebar = render_settings_content