def search4vowels(phrase: str) -> set:
    """
    Display any vowels found in an asked-for phrase.
    """

    # Набір всіх голосних англійської абетки
    vowels = set("aeiou")

    # set(phrase) перетворює фразу на множину унікальних символів
    # intersection() повертає голосні, які зустрічаються у фразі
    # return — множина знайдених голосних
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """
    Display any letters found in an asked-for phrase.
    """
    # привласнення аргументу можливе за позиціями аргументу або за ключем аргументу.

    # привласнення типу: str вказує, що параметр повинен бути рядком. Це допомагає з читабельністю коду і може бути використано для статичної перевірки типів.

    # letters: str = 'aeiou' — це параметр за замовчуванням, який дозволяє користувачу вказати власний набір символів для пошуку. Якщо користувач не надає цей параметр, буде використовуватися набір голосних.
   
    # set(letters) перетворює набір шуканих символів на множину

    # intersection() повертає ті літери, які є і в letters, і в phrase
    
    # return— множина знайдених літер
    return set(letters).intersection(set(phrase))

