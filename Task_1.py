# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

numbers = int(input("Enter a three-digit number: "))
s = 0
for i in range(3):
    s += numbers % 10
    numbers = numbers // 10
print(f"The sum of the digits of this number is equal to : {s}")