# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import math
def multpair(mylist):
    return[mylist[i] * mylist[-i - 1] for i in range(math.ceil(len(mylist)/2))]

mylist = [2, 3, 4, 5, 6]

print (f'1 способ: {multpair(mylist)}')

result = []
for i in range (math.ceil(len(mylist)/2)):
    result.append(mylist[i]*mylist[len(mylist)-1-i])
print(f'2-й способ: {result}')