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

# cinema_genres = ("Комедия", "Экшн", "Пеплум", "Триллер")
# # user_input =input()
# user_input = "Боевик"
# user_replace = "Экшн"
# new_tuple = ""
# for genge in cinema_genres:
#     if genge == user_replace:
#         new_tuple+=" "+user_input
#         new_tuple+=" Аниме"
#     else:
#         new_tuple+=" "+genge
#
#
# print(tuple(new_tuple.split()))
# print("Обновленые жанры кино:",new_tuple)


# 3 task


# my_things = {"axe", "boots", 'apple', "book", "lighter" "boat"}
# he_things = {"axe","monkey","apple","book","dog","rope"}
#
# my_and_he_things = my_things.union(he_things)
# onlY_my_tings = my_things.difference(he_things)
# onlY_he_tings = he_things.difference(my_things)
# my_and_he_only = my_things.intersection(he_things)
# print(my_and_he_things)
# print(onlY_my_tings)
# print(onlY_he_tings)
# print(my_and_he_only)


# 4 task


cinema_genres = ["комедия", "экшн", "пеплум", "триллер", "комедия", "пеплум"]
cinema_genres = set(cinema_genres)
new_genres = {"драма", "Хорор"}
print(cinema_genres)
cinema_genres = cinema_genres.union(new_genres)
print(cinema_genres)
cinema_genres.discard("экшн")
print(cinema_genres)
print(cinema_genres.pop())
print(list(cinema_genres))
