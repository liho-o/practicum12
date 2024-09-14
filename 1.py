text = 'texxxxt   text    text     dfg     fdg'


result = 0
for i in range(1, len(text)):
    symbols = i * ' '
    spaces = text.count(symbols)
    if spaces != 0:
        result = i

print(result)
