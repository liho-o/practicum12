text = input('Введите текст - ')


# text = text.replace(' ', '') #если пробел не считается символом


def ex3_check(text : str):
    for i in text:
        if text.count(i) == 3:
            return i

    return "нет таких символов"


print(ex3_check(text))
