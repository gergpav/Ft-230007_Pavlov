a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
summa = a + b
raznost = a - b
proizved = a * b
sredn_arifm = (a + b) / 2
razn_max_min = max(abs(a), abs(b)) - min(abs(a), abs(b))
print(f'Сумма чисел: {summa}')
print(f'Разность чисел: {raznost}')
print(f'Произведение чисел: {proizved}')
print(f'Среднее арифметическое чисел: {sredn_arifm}')
print(f'Разность максимального и минимального по модулю чисел: {razn_max_min}')