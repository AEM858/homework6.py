print('Сколько одинаковых чисел имеется')
first = int(input('Введите число:'))
second = int(input('Введите число:'))
third = int(input('Введите число:'))
if first == second == third:
    print(3)
elif first == second and second != third:
    print(2)
elif second == third and second != first:
    print(2)
elif first == third and second != first:
    print(2)
else:
    print(0)