# === Типи даних ===
# str (рядок) - слово "bottles" / "bottle"
# int (ціле число) - лічильник пляшок

# === Функції ===
# range(start, stop, step) - генерує послідовність чисел
# range(99, 0, -1) - від 99 до 1 з кроком -1 (спадання)
# print() - виводить дані на екран

# === Умовний оператор ===
# if / else - перевірка умови
# == - оператор рівності

word = "bottles"

# Цикл for - ітерація від 99 до 1 (зворотний порядок)
for beer_num in range(99, 0, -1):
    # Виводимо кількість пляшок на стіні
    print(beer_num, word, "of beer on the waal")

    # Виводимо повідомлення про пляшку
    print(beer_num, word, "of beer.")

    # Інструкція: взяти одну
    print("Take one down")

    # Інструкція: передати
    print("Pass it around")

    # Перевірка: чи це остання пляшка?
    if beer_num == 1:
        # Особливе повідомлення для однієї пляшки
        print("No more bottles of beer on the wall.")
    else:
        # Зменшуємо лічильник на 1
        new_num = beer_num - 1
         
        # Якщо залишилась 1 пляшка - змінюємо форму слова
        if new_num == 1:
            word = "bottle"
        
        # Виводимо скільки залишилось
        print(new_num, word, "of beer on the wall")
    
    # Порожній рядок для розділення куплетів
    print()






