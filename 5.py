a = input('Введите строку для - ')
b = input('Введите строку для - ')
c = input('Введите строку для - ')

aset = set([i for i in a])
bset = set([i for i in b])
cset = set([i for i in c])

uniq_a_symb = ((aset - bset) - cset)
uniq_b_symb = ((bset - aset) - cset)
uniq_c_symb = ((cset - bset) - aset)

result = list(uniq_a_symb) + (list(uniq_b_symb)) + (list(uniq_c_symb))

for symb in set(result):
    print(symb)
