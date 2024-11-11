# task 1
from idlelib.replace import replace
from os.path import split

# genres =("Роман", "Новелла", "Фэнтези", "Научная Фантастика")
# numbers = (3, 7, 9, 1, 6, 8, 2, 5, 4)
#
# print("длина кортежа с жанрами равна :",len(genres),"длина кортежа с цифрами равна :",len(numbers))
# print(max(genres),min(genres),min(numbers),max(numbers))
# print(sum(numbers),"cумма всех чисел")
# print(tuple(sorted(genres)), tuple(sorted(numbers)))
#
# print(tuple(sorted( numbers,reverse=True)), tuple(sorted( genres,reverse=True)))

cinema_genres = ("Комедия", "Экшн", "Пеплум", "Триллер")
# user_input =input()
user_input = "Боевик"
user_replace = "Экшн"
new_tuple = ""
# for genge in cinema_genres:
#     if genge == user_replace:
#         new_tuple+=" "+user_input
#     else:
#         new_tuple+=" "+genge

# print(tuple(new_tuple.split()))
#2 вариант решения
# new_tuple = " ".join(cinema_genres)
# new_tuple = new_tuple.replace(user_replace, user_input).split()
# print(tuple(new_tuple))

#3 вариант решения

new_tuple = tuple(user_input if genre==user_replace else genre for genre in cinema_genres)
print(new_tuple)