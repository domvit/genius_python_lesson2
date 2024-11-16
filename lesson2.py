# 1. Створити змінні таких типів: string, integer, float, bool, list, dict, tuple, None
string_variable_1 = "String1"
string_variable_2 = "String2"

integer_variable_1 = 1
integer_variable_2 = 2

float_variable_1 = 1.0
float_variable_2 = 3.1415926

bool_variable_1 = True
bool_variable_2 = False

list_variable_1 = [1, 2, 3]
list_variable_2 = [1, 2, 3, 4]

dict_variable_1 = {"a": 1, "b": 2, "c": 3}
dict_variable_2 = {"x": 1, "y": 2, "z": 3}

tuple_variable_1 = (1, 2, 3)
tuple_variable_2 = (4, 2, 3, "546")

none_variable = None

# 2. Використати вивчені оператори та порівняти між собою числа, рядки, булеві значення, списки, словники і кортежі
print('equal sting',string_variable_1 == string_variable_2)
print('equal integer',integer_variable_1 == integer_variable_2)
print('equal float',float_variable_1 <= float_variable_2)
print('equal numbers integer_variable_1 and float_variable_1',integer_variable_1 == float_variable_1)
print('equal boolean',bool_variable_1 != bool_variable_2)
print('equal list',list_variable_1 < list_variable_2)
print('equal dict',dict_variable_1 != dict_variable_2)
print('equal tuple 1',tuple_variable_1 == tuple_variable_1)
print('equal tuple 2', len(tuple_variable_1) == len(tuple_variable_2))


# 3. Використати вивчені функції Python:
# Робота з рядками:
#  1. Cтворити змінну num_str = 125, перевести її в тип string за допогою функції str()
num_str = 125
num_str = str(num_str)
print(type(num_str))

#  2. Cтворити зміну message = 'Hi, my name is Python!' За допомогою функції replace() замінити
# усі букви 'y' на '0' та 'i' на '1'.
message = 'Hi, my name is Python!'
print('message before:', message)
message = message.replace('y', '0').replace('i', '1')
print('message after:', message)

#  3. Cтворити зміну split_test = 'This is a split test' і розділити її по пробілах за
# допомогою функції split(), а потім знову обʼєднати у строку за допомогою функції join() у змінну string_join
split_test = 'This is a split test'
print('split test before:', split_test)
split_test = split_test.split()
print('split test after:', split_test)
string_join = ' '.join(split_test)
print('string join:', string_join)

#  4. Визначити довжину рядку string_join за допомогою функції len()
len_string_join = len(string_join)
print('length string_join:', len_string_join)

# Робота зі списками:
#  1. Cтворити змінну list_append = [1, 2, 3] і за допомогою функції append() додати туди спочатку 4, а потім 5
list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)
print('list_append:', list_append)

#  2. Cтворити змінну list_extend = [4, 5, 6] і розширити цей список іншим списком [7, 8, 9] за допомогою функції extend()
list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])
print('list_extend:', list_extend)
#  3. Визначити індекс елемента 6 у списку list_extend за допомогою функції index()
list_index_6 = list_extend.index(6)
print('list_index_6:', list_index_6)
#  4. Визначити довжину списку list_append за допомогою функції len()
len_list_extend = len(list_extend)
print('len_list_extend:', len_list_extend)

# Робота зі словниками:
#  1. Cтворити змінну dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'} та вивести на екран дані, які знаходяться в ключах car та where
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print("dict_test['car']:", dict_test['car'])
print("dict_test['where']:", dict_test.get('where'))
#  2. За допомогою функцій keys() і values() вивести на екран ключі та їх значення
print("dict_test keys:", dict_test.keys())
print("dict_test values:", dict_test.values())
#  3. За допомогою функції items() вивести на екран пари ключ - значення
print("dict_test items:", dict_test.items())
