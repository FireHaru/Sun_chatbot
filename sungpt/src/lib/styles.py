"""
src/lib/styles.py
Toàn bộ CSS custom cho giao diện SunGPT
"""
import streamlit as st


def inject_styles():
    """Inject CSS tùy chỉnh vào Streamlit"""
    st.markdown("""
<style>
/* ===== IMPORT FONTS ===== */
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

/* ===== ROOT VARIABLES ===== */
:root {
    --bg-primary: #0f0f0f;
    --bg-sidebar: #171717;
    --bg-chat: #212121;
    --bg-input: #2f2f2f;
    --bg-hover: #2a2a2a;
    --bg-card: #1e1e1e;
    --bg-code: #1a1a2e;

    --accent-primary: #f59e0b;
    --accent-hover: #fbbf24;
    --accent-light: rgba(245, 158, 11, 0.15);
    --accent-glow: rgba(245, 158, 11, 0.3);

    --text-primary: #ececec;
    --text-secondary: #8e8ea0;
    --text-muted: #565869;
    --text-accent: #f59e0b;

    --border: rgba(255,255,255,0.08);
    --border-accent: rgba(245, 158, 11, 0.4);

    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 16px;
    --radius-xl: 24px;

    --font-main: 'Sora', sans-serif;
    --font-mono: 'JetBrains Mono', monospace;

    --shadow-accent: 0 0 20px rgba(245, 158, 11, 0.2);
    --transition: all 0.2s ease;
}

/* ===== GLOBAL RESET ===== */
* { box-sizing: border-box; }

.stApp {
    background: var(--bg-primary) !important;
    font-family: var(--font-main) !important;
    color: var(--text-primary) !important;
}

/* ===== HIDE STREAMLIT DEFAULTS ===== */
#MainMenu { visibility: hidden !important; }
footer { visibility: hidden !important; }
.stDeployButton { display: none !important; }
[data-testid="stDecoration"] { display: none !important; }
[data-testid="stStatusWidget"] { display: none !important; }
.viewerBadge_container__1QSob { display: none !important; }

/* ÉP HIỂN THỊ THANH TASKBAR ĐỂ GIỮ NÚT ĐIỀU KHIỂN GỐC */
[data-testid="stToolbar"] { 
    display: flex !important; 
    visibility: visible !important;
    opacity: 1 !important;
}

/* ===== SIDEBAR TOGGLE — luôn hiện nút kéo sidebar ===== */
[data-testid="stSidebarCollapsedControl"] {
    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
    position: fixed !important;
    top: 14px !important;
    z-index: 9999 !important;
    background: var(--bg-sidebar) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-sm) !important;
    padding: 4px !important;
    transition: var(--transition) !important;
}

[data-testid="stSidebarCollapsedControl"]:hover {
    background: var(--bg-hover) !important;
    border-color: var(--border-accent) !important;
    box-shadow: var(--shadow-accent) !important;
}

/* Nút toggle bên trong sidebar (collapse) */
[data-testid="stSidebar"] [data-testid="stBaseButton-headerNoPadding"],
[data-testid="stSidebar"] button[kind="headerNoPadding"] {
    display: flex !important;
    visibility: visible !important;
    color: var(--text-secondary) !important;
    background: transparent !important;
    border: none !important;
}

/* ===== DISCLAIMER — ghim xuống đáy màn hình ===== */
.disclaimer-fixed {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    text-align: center;
    font-size: 12px;
    color: var(--text-muted);
    padding: 5px 0 7px;
    z-index: 200;
    pointer-events: none;
}

/* Padding bottom cho chat để không bị che bởi disclaimer */
[data-testid="stChatInput"] {
    margin-bottom: 28px !important;
}

/* ===== SIDEBAR ===== */
[data-testid="stSidebar"] {
    background: var(--bg-sidebar) !important;
    border-right: 1px solid var(--border) !important;
    width: 260px !important;
}

[data-testid="stSidebar"] > div:first-child {
    padding: 0 !important;
}

[data-testid="stSidebarContent"] {
    padding: 0 !important;
    background: transparent !important;
}

/* ===== MAIN CONTENT ===== */
.main .block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* ===== SCROLLBAR ===== */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb {
    background: var(--text-muted);
    border-radius: 3px;
}
::-webkit-scrollbar-thumb:hover { background: var(--text-secondary); }

/* ===== SIDEBAR LOGO ===== */
.sungpt-logo {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 16px;
    border-bottom: 1px solid var(--border);
}

.sungpt-logo-icon {
    font-size: 28px;
    filter: drop-shadow(0 0 8px var(--accent-glow));
    animation: sunPulse 3s ease-in-out infinite;
}

@keyframes sunPulse {
    0%, 100% { filter: drop-shadow(0 0 8px var(--accent-glow)); }
    50% { filter: drop-shadow(0 0 16px var(--accent-glow)) brightness(1.2); }
}

.sungpt-logo-text {
    font-size: 18px;
    font-weight: 700;
    color: var(--accent-primary);
    letter-spacing: -0.3px;
}

/* ===== NEW CHAT BUTTON ===== */
.new-chat-btn {
    margin: 12px;
    padding: 10px 14px;
    background: var(--accent-primary);
    color: #000;
    border: none;
    border-radius: var(--radius-md);
    font-family: var(--font-main);
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    width: calc(100% - 24px);
    text-align: left;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: var(--transition);
}

.new-chat-btn:hover {
    background: var(--accent-hover);
    transform: translateY(-1px);
    box-shadow: var(--shadow-accent);
}

/* ===== CONVERSATION LIST ===== */
.conv-section-title {
    font-size: 11px;
    font-weight: 600;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.8px;
    padding: 8px 16px 4px;
}

.conv-item {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 9px 12px;
    margin: 2px 8px;
    border-radius: var(--radius-sm);
    cursor: pointer;
    transition: var(--transition);
    color: var(--text-secondary);
    font-size: 13.5px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.conv-item:hover {
    background: var(--bg-hover);
    color: var(--text-primary);
}

.conv-item.active {
    background: var(--accent-light);
    color: var(--text-primary);
    border-left: 2px solid var(--accent-primary);
}

.conv-item-icon { font-size: 14px; opacity: 0.6; flex-shrink: 0; }
.conv-item-title { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; flex: 1; }

/* ===== CHAT HEADER ===== */
.chat-header {
    background: var(--bg-chat);
    border-bottom: 1px solid var(--border);
    padding: 14px 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: sticky;
    top: 0;
    z-index: 10;
}

.chat-model-badge {
    background: var(--accent-light);
    border: 1px solid var(--border-accent);
    color: var(--accent-primary);
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
}

/* ===== WELCOME SCREEN ===== */
.welcome-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 60vh;
    padding: 40px 24px;
    text-align: center;
    animation: fadeInUp 0.5s ease;
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.welcome-sun {
    font-size: 64px;
    margin-bottom: 20px;
    animation: sunSpin 20s linear infinite, sunPulse 3s ease-in-out infinite;
    filter: drop-shadow(0 0 20px var(--accent-glow));
}

@keyframes sunSpin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

.welcome-title {
    font-size: 36px;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 10px;
    letter-spacing: -0.5px;
}

.welcome-title span { color: var(--accent-primary); }

.welcome-subtitle {
    font-size: 15px;
    color: var(--text-secondary);
    max-width: 500px;
    line-height: 1.6;
    margin-bottom: 40px;
}

/* ===== SUGGESTION CARDS ===== */
.suggestion-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    max-width: 680px;
    width: 100%;
    margin: 0 auto;
}

.suggestion-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    padding: 16px 18px;
    cursor: pointer;
    transition: var(--transition);
    text-align: left;
    display: flex;
    align-items: flex-start;
    gap: 12px;
}

.suggestion-card:hover {
    border-color: var(--border-accent);
    background: var(--bg-hover);
    transform: translateY(-2px);
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}

.suggestion-icon {
    font-size: 20px;
    flex-shrink: 0;
    opacity: 0.8;
}

.suggestion-title {
    font-size: 14px;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 4px;
}

.suggestion-desc {
    font-size: 12.5px;
    color: var(--text-secondary);
    line-height: 1.4;
}

/* ===== CHAT MESSAGES ===== */
.chat-messages {
    padding: 20px 0;
    max-width: 820px;
    margin: 0 auto;
}

.message-wrapper {
    padding: 4px 24px;
    margin-bottom: 4px;
    animation: fadeInMsg 0.3s ease;
}

@keyframes fadeInMsg {
    from { opacity: 0; transform: translateY(8px); }
    to { opacity: 1; transform: translateY(0); }
}

/* User message */
.user-message {
    display: flex;
    justify-content: flex-end;
}

.user-bubble {
    background: var(--bg-input);
    border-radius: var(--radius-lg) var(--radius-lg) 4px var(--radius-lg);
    padding: 12px 18px;
    max-width: 75%;
    font-size: 14.5px;
    line-height: 1.6;
    color: var(--text-primary);
    white-space: pre-wrap;
    word-wrap: break-word;
}

/* Assistant message */
.assistant-message {
    display: flex;
    gap: 14px;
    align-items: flex-start;
}

.assistant-avatar {
    width: 34px;
    height: 34px;
    background: linear-gradient(135deg, var(--accent-primary), #f97316);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
    flex-shrink: 0;
    box-shadow: 0 0 12px var(--accent-glow);
}

.assistant-content {
    flex: 1;
    font-size: 14.5px;
    line-height: 1.7;
    color: var(--text-primary);
    padding-top: 6px;
    max-width: calc(100% - 48px);
}

/* ===== CODE BLOCKS ===== */
.stMarkdown pre {
    background: var(--bg-code) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-md) !important;
    font-family: var(--font-mono) !important;
    font-size: 13px !important;
    padding: 16px !important;
    overflow-x: auto !important;
    position: relative;
}

.stMarkdown code {
    font-family: var(--font-mono) !important;
    font-size: 13px !important;
    background: rgba(245, 158, 11, 0.1) !important;
    border-radius: 4px !important;
    padding: 2px 6px !important;
    color: var(--accent-primary) !important;
}

.stMarkdown pre code {
    background: transparent !important;
    padding: 0 !important;
    color: #e2e8f0 !important;
}

/* ===== INPUT AREA ===== */
.input-container {
    position: sticky;
    bottom: 0;
    background: linear-gradient(transparent, var(--bg-chat) 30%);
    padding: 16px 24px 20px;
}

.input-box-wrapper {
    max-width: 820px;
    margin: 0 auto;
    background: var(--bg-input);
    border: 1px solid var(--border);
    border-radius: var(--radius-xl);
    padding: 12px 16px;
    display: flex;
    align-items: flex-end;
    gap: 10px;
    transition: var(--transition);
}

.input-box-wrapper:focus-within {
    border-color: var(--border-accent);
    box-shadow: 0 0 0 3px var(--accent-light);
}

/* Streamlit textarea override */
[data-testid="stChatInput"] {
    background: var(--bg-input) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-xl) !important;
    color: var(--text-primary) !important;
    font-family: var(--font-main) !important;
    font-size: 14.5px !important;
}

[data-testid="stChatInput"]:focus-within {
    border-color: var(--border-accent) !important;
    box-shadow: 0 0 0 3px var(--accent-light) !important;
}

[data-testid="stChatInputSubmitButton"] {
    background: var(--accent-primary) !important;
    border-radius: 50% !important;
}

/* ===== STREAMLIT CHAT MESSAGES ===== */
[data-testid="stChatMessage"] {
    background: transparent !important;
    padding: 8px 0 !important;
    border: none !important;
}

[data-testid="stChatMessage"][data-testid*="user"] {
    flex-direction: row-reverse !important;
}

/* ===== STREAMLIT BUTTONS ===== */
.stButton button {
    background: var(--accent-primary) !important;
    color: #000 !important;
    border: none !important;
    border-radius: var(--radius-md) !important;
    font-family: var(--font-main) !important;
    font-weight: 600 !important;
    transition: var(--transition) !important;
    cursor: pointer !important;
}

.stButton button:hover {
    background: var(--accent-hover) !important;
    transform: translateY(-1px) !important;
    box-shadow: var(--shadow-accent) !important;
}

/* Secondary buttons */
.stButton.secondary button {
    background: transparent !important;
    color: var(--text-secondary) !important;
    border: 1px solid var(--border) !important;
}

.stButton.secondary button:hover {
    background: var(--bg-hover) !important;
    color: var(--text-primary) !important;
}

/* ===== INPUTS ===== */
.stTextInput input, .stTextArea textarea {
    background: var(--bg-input) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-md) !important;
    color: var(--text-primary) !important;
    font-family: var(--font-main) !important;
}

.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: var(--border-accent) !important;
    box-shadow: 0 0 0 3px var(--accent-light) !important;
}

/* ===== NOTIFICATIONS / ALERTS ===== */
.stAlert {
    background: var(--bg-card) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-md) !important;
    color: var(--text-primary) !important;
}

/* ===== DIVIDER ===== */
hr {
    border-color: var(--border) !important;
    margin: 8px 0 !important;
}

/* ===== SIDEBAR FOOTER ===== */
.sidebar-footer {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    padding: 12px 16px;
    border-top: 1px solid var(--border);
    font-size: 12px;
    color: var(--text-muted);
    text-align: center;
    background: var(--sidebar-bg);
    z-index: 10;
}

/* Sidebar full height */
section[data-testid="stSidebar"] > div {
    position: relative;
    min-height: 100vh;
}

/* Prevent overlap */
section[data-testid="stSidebar"] .block-container {
    padding-bottom: 90px !important;
}



/* ===== LOADING ANIMATION ===== */
.typing-indicator {
    display: flex;
    gap: 5px;
    align-items: center;
    padding: 8px 0;
}

.typing-dot {
    width: 8px;
    height: 8px;
    background: var(--accent-primary);
    border-radius: 50%;
    animation: typingBounce 1.4s ease-in-out infinite;
}

.typing-dot:nth-child(2) { animation-delay: 0.2s; }
.typing-dot:nth-child(3) { animation-delay: 0.4s; }

@keyframes typingBounce {
    0%, 60%, 100% { transform: translateY(0); opacity: 0.4; }
    30% { transform: translateY(-8px); opacity: 1; }
}

/* ===== API KEY SETUP ===== */
.api-setup-container {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 28px;
    max-width: 500px;
    margin: 40px auto;
    text-align: center;
}

.api-setup-icon { font-size: 48px; margin-bottom: 16px; }
.api-setup-title {
    font-size: 22px;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 8px;
}

.api-setup-desc {
    font-size: 14px;
    color: var(--text-secondary);
    line-height: 1.6;
    margin-bottom: 20px;
}

/* ===== COPY BUTTON FOR CODE ===== */
.copy-btn {
    position: absolute;
    top: 8px;
    right: 8px;
    background: var(--bg-hover);
    border: 1px solid var(--border);
    border-radius: 6px;
    color: var(--text-secondary);
    font-size: 12px;
    padding: 4px 8px;
    cursor: pointer;
    opacity: 0;
    transition: var(--transition);
}

pre:hover .copy-btn { opacity: 1; }

/* ===== RESPONSIVE ===== */
@media (max-width: 768px) {
    .suggestion-grid { grid-template-columns: 1fr; }
    .welcome-title { font-size: 28px; }
    .welcome-sun { font-size: 48px; }
}

/* ===== MARKDOWN STYLING ===== */
.assistant-content h1, .assistant-content h2, .assistant-content h3 {
    color: var(--text-primary);
    font-family: var(--font-main);
    margin: 16px 0 8px;
}

.assistant-content h1 { font-size: 20px; }
.assistant-content h2 { font-size: 17px; }
.assistant-content h3 { font-size: 15px; }

.assistant-content ul, .assistant-content ol {
    padding-left: 20px;
    margin: 8px 0;
}

.assistant-content li { margin: 4px 0; }

.assistant-content table {
    border-collapse: collapse;
    width: 100%;
    margin: 12px 0;
    font-size: 13.5px;
}

.assistant-content th {
    background: var(--bg-input);
    color: var(--accent-primary);
    padding: 8px 12px;
    border: 1px solid var(--border);
    font-weight: 600;
}

.assistant-content td {
    padding: 8px 12px;
    border: 1px solid var(--border);
    color: var(--text-secondary);
}

.assistant-content tr:hover td { background: var(--bg-hover); }

/* ===== STREAM CURSOR ===== */
.streaming-cursor::after {
    content: '▋';
    color: var(--accent-primary);
    animation: blink 0.8s ease-in-out infinite;
}

@keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0; }
}

/* ===== SIDEBAR TOGGLE BUTTON (☰) TRONG HEADER ===== */
/* ÉP HIỂN THỊ LẠI CÁC THÀNH PHẦN ĐIỀU KHIỂN ĐÓNG MỞ */
[data-testid="stSidebarCollapsedControl"] {
    display: flex !important;
    visibility: visible !important;
    background-color: transparent !important;
    z-index: 999999 !important;
}

/* Style chung cho nút toggle open/close sidebar */
#open_sidebar_btn button, #close_sidebar_btn button {
    background: var(--bg-input) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-sm) !important;
    color: var(--text-secondary) !important;
    font-size: 16px !important;
    min-width: 36px !important;
    padding: 4px 8px !important;
    transition: var(--transition) !important;
}

#open_sidebar_btn button:hover, #close_sidebar_btn button:hover {
    background: var(--accent-light) !important;
    border-color: var(--border-accent) !important;
    color: var(--accent-primary) !important;
}

section[data-testid="stSidebar"] > div:first-child {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

/* ===== STATUS BAR ===== */
.status-bar {
    font-size: 12px;
    color: var(--text-muted);
    text-align: center;
    padding: 4px 0;
    max-width: 820px;
    margin: 0 auto;
}
</style>
""", unsafe_allow_html=True)