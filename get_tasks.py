import requests
import json
from loader import WEBHOOK_URL, BITRIX_DOMAIN


def get_task_links():
    params = {
        "filter[<STATUS]": 4,  # Только задачи "в процессе"
        "filter[RESPONSIBLE_ID]": 1264,  # ID ответственного
        "order[DEADLINE]": "ASC",  # Сортировка по дедлайну
        "select[]": ["ID", "TITLE", "RESPONSIBLE_ID"],  # Поля, которые мы хотим получить
    }

    response = requests.get(WEBHOOK_URL, params=params)

    if response.status_code == 200:
        try:
            data = response.json()
            if "result" in data and "tasks" in data["result"]:
                tasks = data["result"]["tasks"]
                links = [
                    f"{BITRIX_DOMAIN}/company/personal/user/{task['responsibleId']}/tasks/task/view/{task['id']}/"
                    for task in tasks
                ]
                # Сохранение задач в файл
                with open("tasks.json", "w", encoding="utf-8") as file:
                    json.dump(links, file, indent=4, ensure_ascii=False)
                print("Задачи успешно сохранены в tasks.json")
            else:
                print("Ошибка: задачи отсутствуют или структура ответа изменилась.")
        except ValueError as e:
            print("Ошибка преобразования ответа в JSON:", e)
    else:
        print(f"Ошибка API: {response.status_code}, текст ошибки: {response.text}")

if __name__ == "__main__":
    get_task_links()
