text = 'Дано предложение. Найти длину его самого короткого слова.'

# text = text.replace(',', '')
# text = text.replace('.', '')
# text = text.replace('!', '')
# text = text.replace('?', '')

words = text.split()


min_length = len(text)

for word in words:
    if len(word) < min_length:
        min_length = len(word)


print(min_length)