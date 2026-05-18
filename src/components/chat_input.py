"""
src/components/chat_input.py
Input area phía dưới
"""
import streamlit as st


def render_chat_input() -> str | None:
    """
    Render ô nhập liệu chat.
    Trả về message nếu user submit, None nếu chưa.
    """
    prompt = st.chat_input(
        placeholder="Hỏi SunGPT về code...",
        key="chat_input_box",
        disabled=st.session_state.get("is_generating", False),
    )
    return prompt


def render_input_footer():
    """Footer disclaimer ghim dưới cùng màn hình"""
    st.markdown("""
    <div class="disclaimer-fixed">
        ☀️ SunGPT có thể mắc lỗi. Hãy kiểm tra lại các thông tin quan trọng.
    </div>
    """, unsafe_allow_html=True)
