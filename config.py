# Telegram Bot Settings
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
ALLOWED_USER_ID = 123456789  # Ваш Telegram ID

# AI Settings
AI_API_KEY = "your-openai-api-key"  # Опционально
DEBUG_MODE = True

# Termux Settings
TERMUX_TMP = "/data/data/com.termux/files/usr/tmp"
OUTPUT_DIR = TERMUX_TMP if os.path.exists(TERMUX_TMP) else os.path.expanduser("~/yt_downloads")
