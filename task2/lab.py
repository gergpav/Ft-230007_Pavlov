imya = str(input('Имя: '))
vozrast = int(input('Возраст: '))
shkola = int(input('Номер школы: '))
klass = int(input('Какой класс окончил: '))
if klass == 9:
    god = 2024 - (vozrast - 16)
else:
    god = 2024 - (vozrast - 18)
print(f'Привет {imya}!\nПоздравляю с окончанием {klass} класса школы №{shkola} в {god} году.')