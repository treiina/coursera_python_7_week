# Словарь синонимов


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


N = int(input())
dictionary = {}
last_word = ''
while True:
    words = input().split()
    if len(words) == 1:
        if words[0] in dictionary.values():
            last_word = get_key(dictionary, words[0])
        else:
            last_word = dictionary[words[0]]
        break
    else:
        dictionary[words[0]] = words[1]
print(last_word)
