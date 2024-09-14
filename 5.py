a = 'gdfgdfgfdgdfgukyk' #символы только из этой строки
b = 'upoooipiiuiyuioo'
c = 'dslklcmckxjvsoijgre'

aset = set([i for i in a])
bset = set([i for i in b])
cset = set([i for i in c])

uniq_a_symb = (aset - bset) - cset

for symb in uniq_a_symb:
    print(symb)