text = input('Введите предложение - ')

text = text.replace(',', '')
text = text.replace('.', '')
text = text.replace('!', '')
text = text.replace('?', '')

words = text.split()

for word in set(words):
    words.remove(word)

twince_repeted_word = words[0]


print(twince_repeted_word)