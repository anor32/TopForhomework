from englishUtils import get_user_level
from englishUtils import base_program
from englishUtils import get_result
from englishUtils import read_file_with_user_input
from englishUtils import write_stats

python_data = read_file_with_user_input("user_inputs.json")
if python_data == {}:
    user_name = input("введите ваше имя")
    dificulty = input("выберете уровень сложности  легкий  средний сложный :").strip().lower()
else:
    user_name, dificulty = python_data.values()

user_level = get_user_level(dificulty)
answers = base_program(user_level)
result = get_result(answers)
print("ваш Ранг", result)

write_stats(user_name,user_level,result)

# возможно функции для прочитывания файла
# не надо было  заводить  в отдельный файл ну  я решил так
# я стараюсь в основном файле как можно меньше строк делать
# я сделал файл user_inputs для имитации файлов которые будут приходить от внешних источников
# в задании ничего не скзано проних как они должны приходить в сколько слов какие ключи и тд
# поэтому я сделал на свое усмотрение
# я так полагаю главное тут было прочитать файл и взять из него данные  ну и конвертировать