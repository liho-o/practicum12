text = 'Дано предложение. Напечатать его в обратном порядке слов.'

text_list = text.split()


for word in text_list[::-1]:
    print(word, end=' ')