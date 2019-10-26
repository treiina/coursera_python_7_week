# Количество слов в тексте
import sys
text = sys.stdin.read()
f = open('text.txt', 'w')
f.write(text)
f.close()
print(len(set(open('text.txt').read().split())))
