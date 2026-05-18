"""
src/components/api_setup.py
Giao diện setup API key lần đầu
"""
import streamlit as st
import os
from src.api.gemini_client import create_model


def render_api_setup():
    """Hiển thị form nhập API key nếu chưa có"""
    st.markdown("""
    <div class="api-setup-container">
        <div class="api-setup-icon">🔑</div>
        <div class="api-setup-title">Cài đặt API Key</div>
        <div class="api-setup-desc">
            SunGPT cần Gemini API key để hoạt động.<br>
            Lấy miễn phí tại <strong>aistudio.google.com</strong>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        api_key = st.text_input(
            "Gemini API Key",
            type="password",
            placeholder="AIza...",
            help="Lấy API key tại https://aistudio.google.com/app/apikey"
        )

        if st.button("🚀 Kết nối SunGPT", use_container_width=True):
            if api_key:
                os.environ["GEMINI_API_KEY"] = api_key
                model = create_model()
                if model:
                    st.session_state.model = model
                    st.session_state.api_key_set = True
                    st.success("✅ Kết nối thành công! SunGPT sẵn sàng.")
                    st.rerun()
                else:
                    st.error("❌ API key không hợp lệ. Vui lòng thử lại.")
            else:
                st.warning("⚠️ Vui lòng nhập API key.")

        st.markdown("""
        <div style="text-align:center;margin-top:16px">
            <a href="https://aistudio.google.com/app/apikey" 
               target="_blank" 
               style="color:var(--accent-primary);font-size:13px;text-decoration:none">
                📎 Lấy API key miễn phí →
            </a>
        </div>
        """, unsafe_allow_html=True)
