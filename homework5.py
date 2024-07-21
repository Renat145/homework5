immutable_var = (1, 2, 3, False, 'apple')
print(immutable_var)
print(immutable_var[0])
# пример: immutable_var[0] = 5. изменить элемент в кортеже не получится, программа выдаст ошибку.
# кортеж неизменяемый. хотя внутри кортежа можно добавить список (в квадратных скобках),
# внутри которого можно будет изменять элементы

mutable_list = [1, 2, 3, False, 'apple']
mutable_list[-1] = 'огурец'
print(mutable_list)