import json
from telethon import TelegramClient
from loader import CHAT_ID, API_HASH, API_ID


async def send_task_links():
    # Загрузка задач из файла
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            task_links = json.load(file)
    except FileNotFoundError:
        print("Файл tasks.json не найден. Сначала выполните скрипт для получения задач.")
        return

    # Создаем клиент
    client = TelegramClient("my_account", API_ID, API_HASH)

    async with client:
        try:
            # Получаем Entity для закрытого канала
            entity = await client.get_entity(int(CHAT_ID))
            print(f"Entity успешно получен: {entity.title}")

            if task_links:
                # Формирование сообщения
                message = "Всем доброе утро! \nСсылки на задачи:\n" + "\n".join(task_links)
                await client.send_message(entity, message)
                print("Сообщение успешно отправлено.")
            else:
                print("Нет задач для отправки.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    from asyncio import run
    run(send_task_links())
