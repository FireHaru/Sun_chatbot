"""
src/hooks/use_chat.py
Hook xử lý logic chat: gửi tin nhắn, nhận response
"""
import streamlit as st
from src.api.gemini_client import stream_response, get_title_from_message
from src.lib.session import (
    add_message, get_current_conversation,
    create_conversation, update_conversation_title
)


def handle_user_message(user_input: str, model):
    """
    Xử lý tin nhắn user:
    1. Tạo conversation nếu chưa có
    2. Thêm tin nhắn vào history
    3. Stream response từ Gemini
    4. Cập nhật title nếu là tin nhắn đầu
    """
    if not user_input.strip():
        return

    # Đảm bảo có conversation
    conv = get_current_conversation()
    if conv is None:
        create_conversation()
        conv = get_current_conversation()

    is_first_message = len(conv["messages"]) == 0

    # Thêm user message
    add_message("user", user_input)

    # Stream response
    st.session_state.is_generating = True
    history = conv["messages"][:-1]  # Exclude tin nhắn vừa thêm

    with st.chat_message("assistant", avatar="☀️"):
        response_placeholder = st.empty()
        full_response = ""

        try:
            for chunk in stream_response(model, history, user_input):
                full_response += chunk
                response_placeholder.markdown(full_response + "▋")
            response_placeholder.markdown(full_response)
        except Exception as e:
            error_msg = f"❌ Lỗi kết nối: {str(e)}\n\nVui lòng kiểm tra API key và thử lại."
            response_placeholder.error(error_msg)
            full_response = error_msg

    # Lưu response
    add_message("assistant", full_response)
    st.session_state.is_generating = False

    # Cập nhật title cho conversation đầu tiên
    if is_first_message:
        try:
            title = get_title_from_message(model, user_input)
            conv_id = st.session_state.current_conv_id
            update_conversation_title(conv_id, title)
        except Exception:
            pass

    st.rerun()
