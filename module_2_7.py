def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(5)
print_params(b=25)
print_params(c=[1, 2, 3])

print('__________')

value_list = [5, 'stroke', None]
values_dict = {'a': 7, 'b': 'fox', 'c': True}
print_params(*value_list)
print_params(**values_dict)

print('__________')

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
