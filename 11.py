"""
Петя и Вася играют в игру "Города". Первым называет город Петя.
Каждый следующий, называемый город должен начинаться на ту букву, на которую окончился предыдущий.
Программа получает на вход строку, состоящую из слов (городов), разделенных пробелами, которые называли игроки.
В результате работы, программа должна определять имя победителя.
Игрок выигрывает, если он назвал слово последним. Однако, игрок проигрывает, если он первым нарушил правила игры.
"""

text = input('Введите строку - ')
words = [i.replace('ь', '') for i in text.split()]


def twin_def(words, i):
    first_word = words[i].lower()
    second_word = words[i + 1].lower()

    if first_word[-1] == second_word[0]:
        return True
    else:
        return False


def winner_check(i):
    if i % 2 == 0:
        return 'Петя'
    else:
        return "Вася"


def mian_fnc(words):
    for i in range(0, len(words) - 1):
        check = twin_def(words, i)

        if check:
            pass
        else:
            winner = winner_check(i + 1)
            print(winner)
            return

    winner = winner_check(i)
    print(winner)


mian_fnc(words)
