# Номер появления слова
import sys
text = sys.stdin.read().split()

text_words = list(set(text))
check = dict.fromkeys(text_words, 0)

for i in text:
    print(check[i], end=' ')
    check[i] += 1
