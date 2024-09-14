text = 'Дано предложение. Напечатать все его слова в порядке неубывания их длин.'

# text = text.replace(',', '')
# text = text.replace('.', '')
# text = text.replace('!', '')
# text = text.replace('?', '')

words = text.split()

for i in range(1, len(text)):
    for ib in words:
        if i == len(ib):
            print(ib)
