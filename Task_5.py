# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint as RD
n = int(input("Введите количество монеток: "))
a = [RD(0,1) for _ in range(n)]

print(*a)

if sum(a) < len(a)-sum(a): print(sum(a))
else: print(len(a)-sum(a))


