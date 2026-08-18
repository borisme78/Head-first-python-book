# Модуль для конвертування часу з 24-годинного формату на 12-годинний
from datetime import datetime
import pprint

# Функція для конвертування часу з 24-годинного на 12-годинний формат
def convert_to_datetime(time24: str) -> str:
    """
    Конвертує час з 24-годинного формату (H:M) на 12-годинний формат (I:M p)
    Приклад: '14:30' -> '02:30 PM'
    """
    return datetime.strptime(time24, "%H:%M").strftime("%I:%M %p")

# Читання даних з CSV файлу та створення словника рейсів
with open('buzzers.csv', 'r') as data:
    lines = data.readline()  # Прочитати заголовок (рядок не використовується)
    flights = {}  # Словник для зберігання: час вильоту -> пункт призначення

    # Обробити кожен рядок файлу
    for line in data:
        k, v = line.strip().split(',')  # Розділити рядок на час та напрямок
        flights[k] = v  # Додати до словника

# Вивести оригінальні дані з 24-годинним форматом часу
pprint.pprint(flights)
print()

# Створити новий словник з конвертованим часом у 12-годинному форматі
fts = {convert_to_datetime(k): v for k,v in flights.items()}

# Вивести дані з 12-годинним форматом часу
pprint.pprint(fts)
print()

# Створити словник де ключ - пункт призначення, значення - список часів прильоту
when = {dest: [k for k,v in fts.items() if v == dest] for dest in set(fts.values())}

# Вивести результат: коли кожна пункт призначення закриває (за 12-годинним форматом)
pprint.pprint(when)
