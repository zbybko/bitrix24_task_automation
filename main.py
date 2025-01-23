import subprocess
import os

def run_script(script_name):
    try:
        print(f"Запуск скрипта: {script_name}")
        result = subprocess.run(
            ["python", script_name],  # Запуск скрипта
            capture_output=True,      # Захват вывода
            text=True,                # Вывод в текстовом формате
            check=True                # Исключение при ошибке выполнения
        )
        print(f"Скрипт {script_name} завершен успешно!")
        print(f"Вывод:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении скрипта {script_name}:")
        print(f"Код ошибки: {e.returncode}")
        print(f"Вывод:\n{e.output}")
    except FileNotFoundError:
        print(f"Скрипт {script_name} не найден!")

if __name__ == "__main__":
    # Список всех скриптов, которые нужно запустить
    scripts = [
        "start_timer.py",        # Начало рабочего дня
        "get_tasks.py",          # Получение задач
        "send_message.py",       # Отправка сообщений
    ]

    # Поочередный запуск всех скриптов
    for script in scripts:
        script_path = os.path.join(os.getcwd(), script)  # Полный путь к скрипту
        run_script(script_path)
