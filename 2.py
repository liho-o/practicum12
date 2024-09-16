text = input('Введите текст - ')

result = 0
for i in range(1, len(text)):
    for d in text:

        symbols = i * d
        repeatlength = text.count(symbols)
        if repeatlength != 0:
            result = i


print(result)

