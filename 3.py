text = input('Введите текст - ')


result = 0

text = text.replace(' ', '')
split_text = [i for i in text if i.isalpha()]

print(len(set(split_text)))