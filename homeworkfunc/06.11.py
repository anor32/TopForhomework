# Задача: Создайте функцию под названием calculate_average , которая принимает переменное количество числовых аргументов
# и возвращает среднее значение этих чисел.

def calculate_average(*args):
   return sum(args)/len(args)


print(calculate_average(10, 20, 30))
# Написать функцию с использованием *args, которая будет принимать
# случайное количество символов, подсчитывать количество повторений отдельных символов
# и возвращать результат в виде частотного словаря символов.




def get_dict(*agrs):
    my_dict={}
    count=1
    for i in agrs:

        if i in my_dict.keys():
            my_dict[i]+=1
        else:
            my_dict[i]=count
    return my_dict


print(get_dict(*"abbbccc"))
print(get_dict(*"abc"))
assert get_dict(*"abbbccc") == {'a': 1, 'b': 3, 'c': 3}
assert get_dict(*"abc") == {'a': 1, 'b': 1, 'c': 1}


#примеры на kwargs

def describe_person (**kwargs):
    for key,value in kwargs.items():
        print(key,value)

describe_person(name="Alice", age=30, occupation="Engineer")