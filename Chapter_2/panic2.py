# === Типи даних ===
# str (рядок) - послідовність символів
# list (список) - впорядкована колекція елементів

# === Срізання списків (slicing) ===
# list[start:end] - елементи від start до end-1
# list[1:3] - елементи з індексами 1 та 2

# === Конкатенація ===
# + - об'єднання рядків
# ''.join() - об'єднання списку елементів у рядок

phrase = "Don't panic!"

# Перетворюємо рядок у список символів
plist = list(phrase)
print(phrase)
print(plist)

# Беремо символи з індексами 1 та 2: "on"
new_phrase = ''.join(plist[1:3])

# Додаємо символи у зворотному порядку: plist[5]=n, [4]=i, [7]=a, [6]=t
# Результат: "onita"
new_phrase = new_phrase + "".join(plist[5] + plist[4] + plist[7] + plist[6])

print(plist)
print(new_phrase)
