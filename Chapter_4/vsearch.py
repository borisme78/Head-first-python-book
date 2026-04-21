def search4vowels():
    """
    Display any vowels found in at asked-for word
    """ 

    vowels = {"a", "e", "i", "o", "u"}

    word = input("Provide a word to search for vowels: ")

    # Метод intersection() - знаходить спільні елементи між двома множинами
    # set(word) - перетворює введений рядок у множину унікальних літер
    found = vowels.intersection(set(word))

    # sorted() - сортує знайдені голосні за алфавітом
    for vowel in sorted(found):
        print("The vowels found in the word are:", vowel)


search4vowels()
