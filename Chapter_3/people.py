# === Модулі ===
# pprint (pretty print) - форматоване виведення складних структур

# === Типи даних ===
# dict (словник) - колекція пар ключ-значення
# Ключі: рядки (Name, Gender, Occupation, Home Planet)
# Значення: рядки або вкладені словники

# === Словники (dict) ===
# Синтаксис: {"key": value, "key2": value2}
# Доступ до значення: dict["key"] або dict.get("key")

# Імпортуємо модуль pprint для красивого виведення
import pprint

# Створюємо словники для кожного персонажа
# Кожен персонаж - це словник з полями: Name, Gender, Occupation, Home Planet
Ford = {"Name": "Ford Prefect", "Gender": "Male", "Occupation": "Researcher", "Home Planet": "Betelgeuse Seven"}
Arthur = {"Name": "Arthur Dent", "Gender": "Male", "Occupation": "Sandwich Maker", "Home Planet": "Earth"}
Trillian = {"Name": "Trician McMillan", "Gender": "Female", "Occupation": "Mathematician", "Home Planet": "Earth"}
Robot = {"Name": "Marvin", "Gender": "Unknown", "Occupation": "Paranoid Android", "Home Planet": "Unknown"}

# Порожній словник для зберігання всіх персонажів
people = {}

# Додаємо кожного персонажа в словник people
# Ключ - ім'я персонажа, значення - словник з даними
people["Ford"] = Ford
people["Arthur"] = Arthur
people["Trillian"] = Trillian
people["Robot"] = Robot

# Виводимо весь словник у форматованому вигляді
pprint.pprint(people)

# Доступ до вкладеного словника: people["Arthur"] - це словник
# ['Occupation'] - доступ до ключа всередині цього словника
pprint.pprint(people["Arthur"]['Occupation'])
