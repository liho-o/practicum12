
def check_game_number():
    while True:
        try:
            game_number = input('Введите четырехзначное целое число с неповторяющимися цифрами:')
            if (len(str(game_number)) == 4) and (game_number == str(int(game_number))):
                numbers = [int(i) for i in game_number]
                sorted_numbers = sorted(numbers)
                if sorted(list(set(sorted_numbers))) == sorted_numbers:
                    return int(game_number)
        except ValueError:
            pass

        print('Вы ввели не подходящее число')


def return_count_cows_and_bulls(game_number, round_number):
    bulls = 0
    list_num_game = [int(i) for i in str(game_number)]
    list_num_round = [int(i) for i in str(round_number)]

    for i in range(4):
        if list_num_game[i] == list_num_round[i]:
            bulls += 1

    set_g_num_new = set(list_num_game)
    set_r_num = set(list_num_round)
    for i in set_r_num:
        set_g_num_new.add(i)

    cows = len(list_num_game) + len(set(set_r_num)) - len(set_g_num_new) - bulls
    print(f'Быков: {bulls} Коров: {cows}')


game_number = check_game_number()

for _ in range(25):
    print('\n')


for round_num in range(10):
    round_number = int(input())
    return_count_cows_and_bulls(game_number, round_number)
    if round_number == game_number:
        print('Победа!')
        break

    if round_num == 9:
        print('Проигрыш!')
        break
