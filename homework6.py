my_dict = {'Andrew': 1111, 'Petr': 2222, 'Resha': 3333}
print(my_dict)
print(my_dict['Andrew'])
print(my_dict.get('Dron'))
my_dict.update({'Tor': 4444,
               'Ben': 5555})
del my_dict['Petr']  # Как вывести на экран значение ключа 'Petr' после удаления?

print(my_dict.get('Petr'))
print(my_dict)

my_set = {858, 'laptop', 858, 17.9, 'laptop'}
print(my_set)
my_set.add(1234)
my_set.add('Дорога')
my_set.remove('laptop')

print(my_set)