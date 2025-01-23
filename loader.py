from dotenv import load_dotenv
import os

load_dotenv()

BITRIX24_TASKS_URL = os.getenv("BITRIX24_TASKS_URL")
BITRIX24_DOMAIN = os.getenv("BITRIX24_DOMAIN")
BITRIX24_USER_ID = os.getenv("BITRIX24_USER_ID")
BITRIX24_TIMEMAN_OPEN = os.getenv("BITRIX24_TIMEMAN_OPEN")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")
CHAT_ID = os.getenv("CHAT_TEST_ID")
