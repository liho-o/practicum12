text = 'jnnnnn bnnndulitdd k43333hkjzzk'

result = 0

text = text.replace(' ', '')
split_text = [i for i in text if i.isalpha()]

print(len(set(split_text)))