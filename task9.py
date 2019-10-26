# Самое частое слово
import sys
text = sys.stdin.read().split()
words = {}.fromkeys(text, 0)
for i in text:
    words[i] += 1

list_words = list(words.items())
list_words.sort(key=lambda x: x[1], reverse=True)

words_max = []
for i in list_words:
    if i[1] == list_words[0][1]:
        words_max.append(i[0])
print(sorted(words_max)[0])
