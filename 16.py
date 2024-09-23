"""
Дан текст. Проверить, правильно ли в нем расставлены круглые скобки
(т. е. находится ли справа от каждой открывающей скобки соответствующая ей закрывающая скобка,
а слева от каждой закрывающей — соответствующая ей закрывающая).

"""

text = input('Введите текст')


def in_sk(text, opn_coun=1):
    result = False
    # print('Начал')
    i = 0

    for symbol in text:
        # print(text[i:])
        i += 1
        if symbol == ')':
            clse = True
            opn = bool(opn_coun)
            result = bool(opn * clse)
            # print('Нашел ЗАКРЫВАЮЩУЮ')
            # print('Рез', result)
            clse = False
            opn_coun = opn_coun - 1
            # print(opn_coun)
            if opn_coun != 0:
                result = False

        if symbol == '(':
            opn_coun = opn_coun + 1
            # print("Нашел ОТКРЫВАЮЩУЮ ")
            result = in_sk(text[i:], opn_coun=opn_coun)
            # print(result)

            return result

    return result


def main_check(text):
    i = 0

    for symbol in text:
        # print(symbol)
        i += 1
        if symbol == ')':
            return False
        elif symbol == '(':
            return in_sk(text[i:])


if main_check(text):
    print('OK')
else:
    print('WRONG')
