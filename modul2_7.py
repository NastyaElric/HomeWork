def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)



print_params()
print_params(a = 12, c = False)
print_params(b = 25)
print_params(c = [1,2,3])


def print_params2(a = 1, b = 'строка', c =None):
    values_list = [12, "new", False]
    #values_dict = {a: "cat", b: 21, c: 5.4}
    print(*values_list)


print_params2()

def print_params3(**kwargs):
    for key, value in kwargs.items():
        print(key, value, end= " ")


values_dict = {"a": "cat", "b": 21, "c": 5.4}
print_params3(**values_dict)