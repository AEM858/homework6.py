my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
zero = 0
while len(my_list) > zero:
    if my_list[zero] > 0:
        print(my_list[zero])
        zero = zero + 1
    elif my_list[zero] == 0:
        zero = zero + 1
    else:
        break