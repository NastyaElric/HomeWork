
import random

def select():
    num_ = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    first_num = random.choice(num_)
    return first_num


first_num = select()
print(first_num)

for i in range(1, 21):
    for j in range(2, 21):
        sum_ = i + j
        pairs = [i, j]
        a = first_num
        count = 0
        if first_num % sum_ == 0:
            count = count + 1
            print(*pairs, end=" ")
        else:
            count = 0



