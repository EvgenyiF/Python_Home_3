# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def sort (mylist):    # Убираем из массива целые числа и оставляем только вещественные(иначе минимальное значение дробной части будет 0)
    result = []
    for i in range (len(mylist)):
        if (mylist[i]-int(mylist[i])) != 0:
            result.append(mylist[i])
    return result

mylist = [1.1, 1.2, 3.1, 5, 10.01]

mylist = sort(mylist)
for i in range (len(mylist)):
    mylist[i] = round(mylist[i]-int(mylist[i]),2)
            
print(max(mylist) - min(mylist))