# === Типи даних ===
# str (рядок) - послідовність символів
# list (список) - впорядкована колекція елементів

# === Срізання списків (slicing) ===
# list[:6] - перші 6 елементів (від 0 до 5)
# list[-7:] - останні 7 елементів
# list[12:20] - елементи з індекса 12 до 19

# === Операції з рядками ===
# * n - повторення рядка n разів ( '\t' * 2 = '\t\t')

paranoid_android = "Marvin, the Paranoid Android"
# Перетворюємо рядок у список символів
letters = list(paranoid_android)

# Перші 6 літер імені "Marvin"
for char in letters[:6]:
    print('\t', char)

print()

# Останні 7 літер - "Android"
for char in letters[-7:]:
    print('\t' * 2, char)

print()

# Середня частина - "Paranoid" (індекси 12-19)
for char in letters[12:20]:
    print('\t' * 3, char)