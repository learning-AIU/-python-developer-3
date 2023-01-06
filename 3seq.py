line = input('Введите элементы 1-го списка через запятую: ').split(',')
elements1 = [n.strip() for n in line]
line = input('Введите элементы 2-го списка через запятую: ').split(',')
elements2 = [n.strip() for n in line]

for n in set(elements1) & set(elements2):
    for _ in range(elements1.count(n)):
        elements1.remove(n)

print(*elements1, sep=', ')


# stdout:
# Введите элементы 1-го списка через запятую: 1,2,3,4,5
# Введите элементы 2-го списка через запятую: 2,5
# 1, 3, 4

# Введите элементы 1-го списка через запятую: ab, b,3,cd,x,0
# Введите элементы 2-го списка через запятую: c, d, x, 0, 1
# ab, b, 3, cd
