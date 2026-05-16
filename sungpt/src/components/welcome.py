"""
src/components/welcome.py
Màn hình chào mừng khi chưa có tin nhắn
"""
import streamlit as st
from src.lib.session import get_current_conversation, add_message, create_conversation


SUGGESTIONS = [
    {
        "icon": "💻",
        "title": "Viết code",
        "desc": "Giúp tôi viết hàm sắp xếp mảng bằng Python",
        "prompt": "Giúp tôi viết hàm sắp xếp mảng bằng Python với nhiều thuật toán khác nhau (bubble sort, quick sort, merge sort) và giải thích từng thuật toán."
    },
    {
        "icon": "🐛",
        "title": "Debug lỗi",
        "desc": "Tại sao code JavaScript của tôi bị lỗi undefined?",
        "prompt": "Tại sao code JavaScript hay bị lỗi 'Cannot read properties of undefined'? Giải thích nguyên nhân và cách fix."
    },
    {
        "icon": "📖",
        "title": "Giải thích khái niệm",
        "desc": "REST API là gì và hoạt động thế nào?",
        "prompt": "Giải thích REST API là gì cho người mới bắt đầu. Bao gồm các HTTP methods, status codes và ví dụ thực tế."
    },
    {
        "icon": "✨",
        "title": "Gợi ý cải thiện",
        "desc": "Review và cải thiện code của tôi",
        "prompt": "Hãy hướng dẫn tôi cách viết code Python sạch hơn theo các best practices: naming convention, DRY principle, SOLID principles."
    },
]


def render_welcome():
    """Render màn hình welcome với suggestion cards"""
    st.markdown("""
    <div class="welcome-container">
        <div class="welcome-sun">☀️</div>
        <h1 class="welcome-title">Xin chào, tôi là <span>SunGPT</span></h1>
        <p class="welcome-subtitle">
            Trợ lý AI chuyên biệt cho học tập và lập trình.<br>
            Hãy hỏi tôi bất cứ điều gì về code!
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Suggestion cards — 2x2 grid
    cols = st.columns(2)
    for i, sug in enumerate(SUGGESTIONS):
        with cols[i % 2]:
            card_html = f"""
            <div class="suggestion-card" style="cursor:default">
                <span class="suggestion-icon">{sug['icon']}</span>
                <div>
                    <div class="suggestion-title">{sug['title']}</div>
                    <div class="suggestion-desc">{sug['desc']}</div>
                </div>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)
            if st.button(
                f"Thử ngay →",
                key=f"sug_{i}",
                use_container_width=True,
            ):
                # Tạo conversation mới nếu chưa có
                conv = get_current_conversation()
                if conv is None:
                    create_conversation()

                # Add message vào session và trigger chat
                st.session_state["pending_message"] = sug["prompt"]
                st.rerun()
