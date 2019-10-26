# Встречалось ли число раньше
values = input().split()
check = set()
for i in values:
    if i in check:
        print('YES')
    else:
        print('NO')
        check.add(i)
