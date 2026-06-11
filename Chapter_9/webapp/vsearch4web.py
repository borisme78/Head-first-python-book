# Імпортуємо модулі для веб-додатку та обробки рядків.
# html використовується для безпечного екранування тексту, якщо буде потрібно.
import html

from flask import Flask, redirect, render_template, request
from markupsafe import escape
from vsearch import search4letters  # наша функція для пошуку літер у фразі
from DBcm import UseDatabase  # контекстний менеджер для роботи з БД (не використовується в цьому коді, але може бути корисним для майбутніх змін)
# Створюємо об'єкт Flask, який представляє веб-додаток.
# __name__ допомагає Flask знайти статичні файли та шаблони.
app = Flask(__name__)
    # Параметри підключення до БД
    # ⚠️ У продакшені виносьте це в змінні середовища (os.environ)
app.config['dbconfig'] = {
        'host': '127.0.0.1',
        'user': 'vsearch',
        'password': 'vsearchpasswd',
        'database': 'vsearchlogDB',
    }




def log_request(req: 'flask_request', res: str) -> None:
    """Зберігає дані пошукового запиту та результат у базу даних MySQL."""

    with UseDatabase(app.config['dbconfig']) as cursor:
    # SQL-запит з плейсхолдерами %s — захист від SQL-ін'єкцій
        _SQL = """INSERT INTO log
                (phrase, letters, ip, browser, results)
              VALUES
                (%s, %s, %s, %s, %s)"""

        # Виконуємо запит — підставляємо реальні значення замість %s
        # Виправлено: req.form замість req.from (from — зарезервоване слово)
        # Виправлено: додано пропущену кому після req.form['letters']
        cursor.execute(_SQL, (
        req.form['phrase'],       # пошукова фраза
        req.form['letters'],      # літери для пошуку
        req.remote_addr,          # IP-адреса користувача
        req.user_agent.browser or 'unknown',  # назва браузера або 'unknown' якщо None
        res,                      # результат пошуку
        ))


# Маршрут для обробки POST-запиту форми search4.
# Використовуємо methods=['POST'], щоб дозволити надсилати дані з HTML-форми.
@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    # Отримуємо дані з форми: фразу та літери для пошуку.
    phrase = request.form['phrase']
    letters = request.form['letters']

    title = 'Here are your results:'
    result = str(search4letters(phrase, letters))
    log_request (request, result)
    # Передаємо дані в шаблон results.html для відображення результатів.
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_result=result)


# Два маршрути ведуть на одну сторінку: коренева / та /entry.
# Це дозволяє відкрити форму за обома URL-адресами.
@app.route('/')
@app.route('/entry')
def entry_page() -> str:
    # Повертаємо HTML-сторінку з формою для вводу фрази та літер.
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')

@app.route('/viewlog')

def view_the_log() -> str:
    contents = []

    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """SELECT phrase, letters, ip, browser, results FROM log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()

    titles = ('Phrase', 'Letters', 'Remote_addr', 'Browser', 'Results')

    return render_template('viewlog.html',
                           the_title = 'View Log',
                           the_row_titles = titles,
                           the_data = contents,)


# Запускаємо додаток лише тоді, коли скрипт виконується напряму.
if __name__ == '__main__':
    app.run(debug=True)
