import requests
from loader import BITRIX24_DOMAIN, BITRIX24_USER_ID, BITRIX24_TIMEMAN_OPEN

bitrix24_domain = BITRIX24_DOMAIN
user_id = BITRIX24_USER_ID
webhook = BITRIX24_TIMEMAN_OPEN

url = f'https://{bitrix24_domain}/rest/{user_id}/{webhook}/timeman.open'

response = requests.get(url)

if response.status_code == 200:
    print("Рабочий день начат успешно.")
else:
    print("Ошибка при начале рабочего дня:", response.status_code, response.text)