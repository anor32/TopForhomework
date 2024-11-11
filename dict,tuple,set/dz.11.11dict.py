

genres =("Роман", "Новелла", "Фэнтези", "Научная Фантастика")
numbers = (3, 7, 9, 1, 6, 8, 2, 5, 4)

print("длина кортежа с жанрами равна :",len(genres),"длина кортежа с цифрами равна :",len(numbers))
print(max(genres),min(genres),min(numbers),max(numbers))
print(sum(numbers),"cумма всех чисел")
print(tuple(sorted(genres)), tuple(sorted(numbers)))

print(tuple(sorted( numbers,reverse=True)), tuple(sorted( genres,reverse=True)))