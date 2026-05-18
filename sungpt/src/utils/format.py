"""
src/utils/format.py
Các hàm format text, timestamp, ...
"""
from datetime import datetime


def truncate_text(text: str, max_len: int = 40) -> str:
    """Cắt ngắn text nếu quá dài"""
    if len(text) <= max_len:
        return text
    return text[:max_len].rstrip() + "..."


def format_timestamp(dt: datetime) -> str:
    """Format datetime thành string dễ đọc"""
    if not dt:
        return ""
    now = datetime.now()
    diff = now - dt

    if diff.seconds < 60:
        return "vừa xong"
    elif diff.seconds < 3600:
        mins = diff.seconds // 60
        return f"{mins} phút trước"
    elif diff.days == 0:
        return dt.strftime("%H:%M")
    elif diff.days == 1:
        return "Hôm qua"
    else:
        return dt.strftime("%d/%m/%Y")


def estimate_tokens(text: str) -> int:
    """Ước tính số tokens (đơn giản: ~4 ký tự = 1 token)"""
    return len(text) // 4


def count_code_blocks(text: str) -> int:
    """Đếm số code blocks trong text"""
    return text.count("```") // 2
