text = input('Введите предложение - ')

text = text.replace(',', '')
text = text.replace('.', '')
text = text.replace('!', '')
text = text.replace('?', '')

words = text.split()

first_word = words[0]


def double_letter_check(word):
    letters = [l for l in word]
    letters_set = set(letters)

    if len(letters_set) == len(letters):
        return True
    else:
        return False


for word in words:
    if word != first_word:
        if double_letter_check(word):
            print(word)
