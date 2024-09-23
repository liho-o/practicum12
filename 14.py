tip = input('Введите подсказку:')
word = input('Введите слово:')

for _ in range(25):
    print('\n')

print(tip)

roundtext = 'Буква или слово (0 - буква, 1 - слово)?'

round_word = len(word) * '*'
print(round_word)

rounds_letters = []

result = 'Проигрыш!'


def return_round_word(letter):
    letters = [i for i in word]
    for letter in letters:
        if letter in rounds_letters:
            print(letter, end='')
        else:
            print('*', end='')
    print('\n')


def round_function(choice, player_input):
    if choice == 1:
        if player_input == word:
            result = 'Победа!'
        else:
            result = 'Проигрыш!'

        print(result)
        return True
    elif choice == 0:
        return_round_word(player_input)


for round_num in range(10):
    choice = int(input(roundtext))
    player_input = input()
    rounds_letters.append(player_input)
    if round_function(choice, player_input):
        break
    else:
        pass
