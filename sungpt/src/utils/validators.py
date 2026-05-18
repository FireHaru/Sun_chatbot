"""
src/utils/validators.py
Validation helpers
"""
import re


def is_valid_api_key(key: str) -> bool:
    """Kiểm tra format của Gemini API key"""
    if not key:
        return False
    # Gemini API keys thường bắt đầu với 'AIza' và dài ~39 ký tự
    return bool(re.match(r'^AIza[0-9A-Za-z\-_]{35}$', key.strip()))


def is_code_related(message: str) -> bool:
    """Kiểm tra tin nhắn có liên quan đến code không"""
    code_keywords = [
        'code', 'lỗi', 'error', 'bug', 'function', 'hàm', 'class',
        'python', 'javascript', 'java', 'c++', 'sql', 'api', 'debug',
        'thuật toán', 'algorithm', 'database', 'frontend', 'backend'
    ]
    message_lower = message.lower()
    return any(keyword in message_lower for keyword in code_keywords)
