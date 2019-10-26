# Частотный анализ
import sys
text = sys.stdin.read().split()
words = {}.fromkeys(text, 0)
for i in text:
    words[i] += 1

list_words = list(words.items())
list_words.sort(key=lambda x: (-x[1], x[0]))

for i in list_words:
    print(i[0])
