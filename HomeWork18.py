#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#*Пример:*

#5
#    1 2 3 4 5
#   6
#    -> 5

from random import randint
n = int(input('Введите кол-во элементов в массиве = '))

list_1 = [randint(1, 10) for _ in range(n)]
print(list_1)
x = int(input('Введите какое число будем проверять  = '))
counter = 0
y = 0
for i in range(n):
    if list_1[i] == x:
        print(f'Такое число есть в массиве: {x}')
    elif list_1[i]-x==1 or list_1[i]-x==-1:
        y = list_1[i]
        print(f'Такого числа нет, но самое ближайшее к нему число {y}')
        break
    elif list_1[i]-x==2 or list_1[i]-x==-2:
        y = list_1[i]
        print(f'Такого числа нет, но самое ближайшее к нему число {y}')
        break
        
