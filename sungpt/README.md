# ☀️ SunGPT — Trợ lý AI dạy code

> Chatbot AI chuyên biệt cho học tập và lập trình, sử dụng Gemini 2.5 Flash

![SunGPT Demo](https://i.imgur.com/placeholder.png)

## 🚀 Tính năng

- 💬 **Chat real-time** với streaming response
- 🐛 **Debug code** — phân tích lỗi, đề xuất fix
- 📖 **Giải thích khái niệm** lập trình từ cơ bản đến nâng cao
- ✨ **Review code** và gợi ý cải thiện
- 🗂️ **Quản lý lịch sử** chat nhiều conversation
- 🔍 **Tìm kiếm** trong lịch sử conversation
- 📋 **Syntax highlighting** cho code blocks
- 🌙 **Dark mode** theo phong cách ChatGPT
- ⚡ **Gemini 2.5 Flash** — model nhanh, thông minh

## 📁 Cấu trúc dự án

```
sungpt/
├── app.py                      # Entry point chính
├── requirements.txt
├── .env.example
├── .streamlit/
│   └── config.toml             # Streamlit theme config
└── src/
    ├── api/
    │   └── gemini_client.py    # Kết nối Gemini API
    ├── components/
    │   ├── sidebar.py          # Sidebar & conversation list
    │   ├── welcome.py          # Màn hình chào mừng
    │   ├── message_display.py  # Hiển thị tin nhắn
    │   ├── chat_input.py       # Input area
    │   ├── api_setup.py        # Setup API key
    │   └── settings.py         # Panel cài đặt
    ├── hooks/
    │   └── use_chat.py         # Logic xử lý chat
    ├── lib/
    │   ├── session.py          # Quản lý session state
    │   └── styles.py           # CSS tùy chỉnh
    ├── pages/
    │   └── chat_page.py        # Trang chat chính
    └── utils/
        ├── format.py           # Format text, timestamp
        └── validators.py       # Validation helpers
```

## ⚙️ Cài đặt

### 1. Clone và cài dependencies

```bash
git clone <repo-url>
cd sungpt
pip install -r requirements.txt
```

### 2. Lấy Gemini API Key

Truy cập [Google AI Studio](https://aistudio.google.com/app/apikey) để lấy API key miễn phí.

### 3. Cấu hình API Key

**Cách 1: Dùng file .env**
```bash
cp .env.example .env
# Chỉnh sửa .env, thêm API key của bạn
GEMINI_API_KEY=AIza...
```

**Cách 2: Nhập trực tiếp trên giao diện**
Khi chạy app lần đầu, sẽ có form nhập API key.

### 4. Chạy ứng dụng

```bash
streamlit run app.py
```

Truy cập: `http://localhost:8501`

## 💡 Hướng dẫn sử dụng

1. **Nhập API key** tại màn hình đầu tiên (hoặc file .env)
2. **Bắt đầu chat** bằng cách gõ câu hỏi về code
3. **Tạo cuộc trò chuyện mới** bằng nút "✏️ Cuộc trò chuyện mới"
4. **Xem lịch sử** ở sidebar trái
5. **Thay đổi API key** trong phần ⚙️ Cài đặt

## 🛠️ Tech Stack

- **Frontend**: Streamlit + Custom CSS
- **AI Model**: Google Gemini 2.5 Flash
- **Language**: Python 3.10+
- **Libraries**: `google-generativeai`, `streamlit`, `python-dotenv`

## 📝 License

MIT License — Tự do sử dụng và chỉnh sửa.
