# Імпортуємо модулі для веб-додатку та обробки рядків.
# html використовується для безпечного екранування тексту, якщо буде потрібно.
import html

from flask import Flask, redirect, render_template, request
from markupsafe import escape
from vsearch import search4letters  # наша функція для пошуку літер у фразі

# Створюємо об'єкт Flask, який представляє веб-додаток.
# __name__ допомагає Flask знайти статичні файли та шаблони.
app = Flask(__name__)

def log_request(req: 'flask_request', res: str) -> None:
    """Логування даних запиту та результату в файл."""
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

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

    with open('vsearch.log', 'r', encoding='utf-8') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')

    return render_template('viewlog.html',
                           the_title = 'View Log',
                           the_row_titles = titles,
                           the_data = contents,)


# Запускаємо додаток лише тоді, коли скрипт виконується напряму.
if __name__ == '__main__':
    app.run(debug=True)
