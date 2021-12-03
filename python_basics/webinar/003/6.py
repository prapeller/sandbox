def capitalize_words(string_to_capitalize):
    def int_func(word_to_capitalize):
        return word_to_capitalize.capitalize()

    return ' '.join(int_func(word) for word in string_to_capitalize.split())


print(capitalize_words('turn text into capitalized text'))
