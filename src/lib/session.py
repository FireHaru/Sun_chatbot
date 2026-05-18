"""
src/lib/session.py
Quản lý session state của Streamlit
"""
import streamlit as st
import uuid
from datetime import datetime


def init_session():
    """Khởi tạo tất cả session state cần thiết"""
    defaults = {
        "conversations": {},        # {id: {title, messages, created_at}}
        "current_conv_id": None,    # ID conversation đang active
        "model": None,              # Gemini model instance
        "api_key_set": False,       # Đã set API key chưa
        "is_generating": False,     # Đang generate response không
        "show_settings": False,     # Hiện panel settings không
        "search_query": "",         # Query tìm kiếm conversation
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def create_conversation(title: str = "Cuộc trò chuyện mới") -> str:
    """Tạo conversation mới, trả về ID"""
    conv_id = str(uuid.uuid4())
    st.session_state.conversations[conv_id] = {
        "title": title,
        "messages": [],
        "created_at": datetime.now(),
    }
    st.session_state.current_conv_id = conv_id
    return conv_id


def get_current_conversation():
    """Lấy conversation đang active"""
    conv_id = st.session_state.current_conv_id
    if conv_id and conv_id in st.session_state.conversations:
        return st.session_state.conversations[conv_id]
    return None


def add_message(role: str, content: str):
    """Thêm tin nhắn vào conversation hiện tại"""
    conv = get_current_conversation()
    if conv is not None:
        conv["messages"].append({
            "role": role,
            "content": content,
            "timestamp": datetime.now(),
        })


def update_conversation_title(conv_id: str, title: str):
    """Cập nhật tiêu đề conversation"""
    if conv_id in st.session_state.conversations:
        st.session_state.conversations[conv_id]["title"] = title


def delete_conversation(conv_id: str):
    """Xóa một conversation"""
    if conv_id in st.session_state.conversations:
        del st.session_state.conversations[conv_id]
        if st.session_state.current_conv_id == conv_id:
            # Chuyển sang conversation khác nếu có
            remaining = list(st.session_state.conversations.keys())
            st.session_state.current_conv_id = remaining[0] if remaining else None


def get_all_conversations():
    """Lấy tất cả conversations, sắp xếp theo thời gian mới nhất"""
    convs = st.session_state.conversations
    sorted_convs = sorted(
        convs.items(),
        key=lambda x: x[1]["created_at"],
        reverse=True
    )
    return sorted_convs


def switch_conversation(conv_id: str):
    """Chuyển sang conversation khác"""
    if conv_id in st.session_state.conversations:
        st.session_state.current_conv_id = conv_id
