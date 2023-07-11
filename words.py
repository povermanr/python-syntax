def print_upper_words(words):
    """print seperate lines uppercase

   >>> print_upper_words (['Mabel', 'is', 'silly'])

    """

    for word in words:
        print(word.upper())

def print_upper_words2(words):
    for word in words:
        if words.startswith('e') or words.startswith('E'):
            print(word.upper())

def print_upper_words3(words, must_start_with):
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break