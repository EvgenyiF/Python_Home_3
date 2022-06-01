# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('Введите число: '))

# Первый вариант решения
print('Первый вариант решения: ')
print (bin(n).replace('0b',''))

# Второй вариант
def convert_dec_to_bin(n):
    bin_num = []
    while n > 0:
        bin_num.insert(0, n % 2)
        n = n // 2
    return bin_num
print('Второй вариант решения: ')
print(convert_dec_to_bin(n))


# Третий вариант 
mylist = []
def decimalToBinary(n):
 
    if(n > 1):
        
        decimalToBinary(n//2)
 
    print(n%2, end = ' ')
print('Третий вариант решения: ')
mylist.append (decimalToBinary(n))
