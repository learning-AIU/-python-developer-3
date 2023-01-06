line = input('Введите элементы списка через запятую: ')
numbers = [
    n_striped
    for n in line.split(',')
    if line.count(n_striped := n.strip()) < 2
]
print(', '.join(numbers))
