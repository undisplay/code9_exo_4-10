def word_to_comma_splited(word):
    str = ""

    for char in word:
        str = str+char+","

    str = str[:-1]

    print(str)

    return str

word_to_comma_splited("hello")