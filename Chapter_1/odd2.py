# === Модулі ===
# datetime - робота з датою та часом
# random - генерація випадкових чисел
# time - робота з часом (затримка)

# === Типи даних ===
# list (список) - непарні числа від 1 до 59
# int (ціле число) - хвилина, лічильник ітерацій

# === Функції модулів ===
# datetime.today().minute - поточна хвилина
# random.randint(a, b) - випадкове ціле число від a до b
# time.sleep(n) - пауза на n секунд
# range(n) - послідовність від 0 до n-1

# === Оператори ===
# in - перевірка наявності в списку

# Імпортуємо модулі
from datetime import datetime       
import random
import time

# Список непарних чисел (непарні хвилини)
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

# Цикл for - повторюємо 5 разів
for i in range(5):  
    # Отримуємо поточну хвилину
    right_this_minute = datetime.today().minute

    # Перевірка: чи хвилина непарна?
    if right_this_minute in odds:
        print("This minute seems a little odd.")
    else:    
        print("Not an odd minute.")
    
    # Генеруємо випадкову затримку від 1 до 60 секунд
    wait_time = random.randint(1, 60)
    # Чекаємо вказану кількість секунд
    time.sleep(wait_time)