from dotenv import load_dotenv
import os

load_dotenv()

WEBHOOK_URL = os.getenv("WEBHOOK_URL")
BITRIX_DOMAIN = os.getenv("BITRIX_DOMAIN")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")
CHAT_ID = os.getenv("CHAT_ID")
