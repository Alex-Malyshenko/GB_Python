# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (
#     т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”,
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
#
# *Пример:*
#
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам
#
#
text = input("Введите фразу Винни-Пуха: ").split()
vowels = set("аеёиоуыэюяАЕЁИОУЫЭЮЯ")

def Check_Vow(string, vowels):
    final = [each for each in string if each in vowels]
    return len(final)

flag = True
if len(text) > 1:
    s = Check_Vow(text[0], vowels)
    for i in text:
        if Check_Vow(i, vowels) != s:
            flag = False
            break
print(("Пам парам","Парам пам-пам")[flag])






