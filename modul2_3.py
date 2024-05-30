my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
number_ = 0
while number_ <  len(my_list):
    if 0 < my_list[number_]:
        print(my_list[number_])
        number_ += 1
    if my_list[number_] == 0:
        number_ += 1
    if my_list[number_] < 0:
        break
