'''
Как известно, имя в языке Python может содержать только латинские символы, цифры и знак подчеркивания "_".
При этом, имя не может начинаться с цифры и не может быть ключевым словом.
Напишите программу, которая проверяет введенную строку, может ли она быть именем в языке Python.
'''

import keyword

text = input('Введите имя переменной - ')


def alphabet_digit_set_check(alp_set):
    for i in alp_set:
        if i.isdigit() or i.isalpha():
            pass
        else:
            return False
    return True


def name_check(name):
    if name[0].isdigit():
        return False
    symbl_name_list = [i for i in name.replace('_', '')]
    symbl_name_set = set(symbl_name_list)
    return alphabet_digit_set_check(symbl_name_set)


if name_check(text):
    print('Все ок')
else:
    print('Недопустимое имя переменной')