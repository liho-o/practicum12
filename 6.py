text = input('Введите предложение - ')


text_list = text.split()


for word in text_list[::-1]:
    print(word, end=' ')