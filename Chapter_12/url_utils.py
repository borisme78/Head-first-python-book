# Імпортуємо бібліотеку requests для виконання HTTP-запитів
import requests

def gen_from_url(urls: tuple) -> tuple:
    """
    Функція-генератор, яка завантажує URL-адреси та повертає інформацію про відповіді.
    
    Аргументи:
        urls (tuple): Кортеж URL-адрес для завантаження
        
    Повертає:
        tuple: Кортеж, що містить (довжина_контенту, код_статусу, url) для кожного запиту
    """
    # Генеруємо HTTP GET-запити для кожної URL-адреси з вхідного кортежу
    for resp in (requests.get(url) for url in urls):
        # Повертаємо довжину контенту, HTTP код статусу та URL-адресу для кожної відповіді
        yield len(resp.content), resp.status_code, resp.url