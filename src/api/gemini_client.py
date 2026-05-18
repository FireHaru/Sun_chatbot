"""
src/api/gemini_client.py
Kết nối và giao tiếp với Gemini 2.5 Flash API
"""
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

SYSTEM_PROMPT = """Bạn là SunGPT — trợ lý AI chuyên biệt về lập trình và học code, được tạo ra bởi SunGPT Team.

## Vai trò của bạn:
- Chuyên gia dạy code với tất cả ngôn ngữ lập trình
- Giải thích khái niệm lập trình từ cơ bản đến nâng cao
- Debug và phân tích lỗi code
- Review code và đề xuất cải thiện
- Hướng dẫn best practices và design patterns

## Phong cách trả lời:
- Luôn dùng code blocks với syntax highlighting khi viết code
- Giải thích ngắn gọn, súc tích nhưng đầy đủ
- Dùng tiếng Việt khi người dùng hỏi tiếng Việt, tiếng Anh khi hỏi tiếng Anh
- Khi debug: chỉ rõ lỗi, nguyên nhân, và cách fix
- Thêm comment vào code để người mới hiểu
- Khi cần thiết, cung cấp nhiều cách giải quyết khác nhau

## Lưu ý:
- Không trả lời các câu hỏi không liên quan đến lập trình, học tập kỹ thuật
- Luôn encourage và tạo động lực cho người học
- Nếu không biết chắc, hãy nói thật thay vì đoán mò"""


def get_gemini_client():
    """Khởi tạo Gemini client với API key"""
    api_key = os.getenv("GEMINI_API_KEY", "")
    if not api_key:
        return None
    genai.configure(api_key=api_key)
    return genai


def create_model():
    """Tạo Gemini 2.5 Flash model với system instruction"""
    client = get_gemini_client()
    if client is None:
        return None
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        system_instruction=SYSTEM_PROMPT,
        generation_config={
            "temperature": 0.7,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
        },
        safety_settings=[
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_ONLY_HIGH"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_ONLY_HIGH"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_ONLY_HIGH"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_ONLY_HIGH"},
        ]
    )
    return model


def build_history(messages: list) -> list:
    """Chuyển đổi lịch sử chat sang định dạng Gemini"""
    history = []
    for msg in messages:
        role = "user" if msg["role"] == "user" else "model"
        history.append({
            "role": role,
            "parts": [msg["content"]]
        })
    return history


def stream_response(model, history: list, user_message: str):
    """Stream response từ Gemini"""
    chat_history = build_history(history)
    chat = model.start_chat(history=chat_history)
    response = chat.send_message(user_message, stream=True)
    for chunk in response:
        try:
            if chunk.text:
                yield chunk.text
        except Exception:
            # Bỏ qua các chunk bị block hoặc rỗng
            continue


def get_title_from_message(model, message: str) -> str:
    """Tạo tiêu đề ngắn cho conversation từ tin nhắn đầu tiên"""
    try:
        prompt = f"Tạo tiêu đề cực ngắn (tối đa 5 từ) cho cuộc trò chuyện bắt đầu bằng: '{message}'. Chỉ trả về tiêu đề, không giải thích."
        response = model.generate_content(prompt)
        return response.text.strip()[:50]
    except Exception:
        return message[:40] + "..." if len(message) > 40 else message
