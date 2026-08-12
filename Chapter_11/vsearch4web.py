"""Flask web app: search for letters and log requests to MySQL.

Цей файл реалізує простий веб-інтерфейс для функції `search4letters`
та зберігає запити у таблицю `log` в MySQL через контекстний менеджер
`UseDatabase` з модуля `DBcm`.
"""

import html

from flask import Flask, copy_current_request_context, redirect, render_template, request, session
from markupsafe import escape
from vsearch import search4letters
from DBcm import UseDatabase, ConnectionError, CredentialsError, SQLError
from checker import check_logged_in
from time import sleep


app = Flask(__name__)

# У реальному проєкті ці значення повинні зчитуватись із змінних оточення
app.secret_key = 'my-secret-key'
app.config['dbconfig'] = {
    'host': '127.0.0.1',
    'user': 'vsearch',
    'password': 'vsearchpasswd',
    'database': 'vsearchlogDB',
}


def log_request(req: 'flask_request', res: str) -> None:
    """Записує дані запиту у таблицю `log`.

    Використовує плейсхолдери для запобігання SQL-ін'єкціям.
    """

    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = ("""INSERT INTO log
                (phrase, letters, ip, browser, results)
              VALUES
                (%s, %s, %s, %s, %s)""")

        cursor.execute(_SQL, (
            req.form['phrase'],
            req.form['letters'],
            req.remote_addr,
            req.user_agent.browser or 'unknown',
            res,
        ))


@app.route('/login')
def do_login() -> str:
    """Встановлює сесію користувача як увійшовшого в систему (демо)."""
    session['logged_in'] = True
    return 'You are now logged in.'


@app.route('/logout')
def do_logout() -> str:
    """Видаляє сесію користувача (демо)."""
    session.pop('logged_in', None)
    return 'You are now logged out.'


@app.route('/search4', methods=['POST'])
@check_logged_in
def do_search() -> 'html':
    """Обробляє форму: виконує пошук та рендерить результати.

    Всередині є внутрішня функція `log_request`, обгорнута
    `copy_current_request_context`, що дозволяє виконувати логування
    у контексті запиту (корисно для фонового логування).
    """

    @copy_current_request_context
    def log_request(req: 'flask_request', res: str) -> None:
        # Демонстраційна затримка — у реальному застосунку не блокувати
        sleep(15)
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = ("""INSERT INTO log
                    (phrase, letters, ip, browser, results)
                  VALUES
                    (%s, %s, %s, %s, %s)""")
            cursor.execute(_SQL, (
                req.form['phrase'],
                req.form['letters'],
                req.remote_addr,
                req.user_agent.browser or 'unknown',
                res,
            ))

    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    result = str(search4letters(phrase, letters))

    # Ставимо логування у try/except — воно не повинно ламати основний флоу
    try:
        log_request(request, result)
    except Exception as err:
        print('***** Logging failed with this error:', str(err))

    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_result=result)


@app.route('/')
@app.route('/entry')
def entry_page() -> str:
    """Повертає сторінку з формою для введення фрази та літер."""
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
@check_logged_in
def view_the_log() -> str:
    """Повертає HTML-сторінку з вмістом таблиці `log`.

    Обробляємо можливі помилки підключення/креденшелів/SQL через try/except.
    """
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """SELECT phrase, letters, ip, browser, results FROM log"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()

        titles = ('Phrase', 'Letters', 'Remote_addr', 'Browser', 'Results')

        return render_template('viewlog.html',
                               the_title='View Log',
                               the_row_titles=titles,
                               the_data=contents,)
    except ConnectionError as err:
        print('Is your database switched on? Error:', str(err))
    except CredentialsError as err:
        print('User-id/Password issues. Error:', str(err))
    except SQLError as err:
        print('Is your query correct? Error:', str(err))
    except Exception as err:
        print('Something went wrong:', str(err))
    return 'Error'


if __name__ == '__main__':
    app.run(debug=True)
