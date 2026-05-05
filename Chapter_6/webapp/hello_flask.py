from flask import Flask
from vsearch import search4letters

# Створюємо об'єкт Flask для веб-додатку.
# __name__ допомагає Flask знайти шаблони та статичні файли.
app = Flask(__name__)

# Маршрут для головної сторінки.
# Коли користувач відкриває кореневу адресу, викликається функція hello().
@app.route('/')

def hello() -> str:
    return 'Hello world from Flask!'

# Маршрут для демонстрації функції search4letters.
# Звернення до /search4 повертає результат пошуку літер у прикладі рядку.
@app.route('/search4')

def do_search() -> str:
    # Виконуємо пошук літер у заданому рядку та повертаємо результат у вигляді тексту.
    return str(search4letters('life, the universe, and everything', 'eiru'))

# Запускаємо сервер Flask лише тоді, коли файл виконується напряму.
if __name__ == '__main__':
    app.run(debug=True)
