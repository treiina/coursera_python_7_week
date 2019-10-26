# Угадай число
n = int(input())
help_answer = set(range(1, n + 1))
set_answer = set()
while True:
    answer = input()
    if answer == 'HELP':
        break
    elif answer == 'YES':
        help_answer &= set_answer
    elif answer == 'NO':
        help_answer -= set_answer
    else:
        set_answer = set(map(int, set(answer.split())))
for i in sorted(list(help_answer)):
    print(i, end=" ")
