import json
from json import JSONDecodeError

__levels = {"легкий":
                {"family": "семья",
                 "hand": "рука",
                 "people": "люди",
                 "evening": "вечер",
                 "minute": "минута", },
            "cредний": {
                "believe": "верить",
                "feel": "чувствовать",
                "make": "делать",
                "open": "открывать",
                "think": "думать", },
            "сложный": {
                "rural": "деревенский",
                "fortune": "удача",
                "exercise": "упражнение",
                "suggest": "предлагать",
                "except": "кроме", }
            }
__ranks = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично"
}


def get_user_level(level):
    return __levels[level]


def base_program(questions: dict):
    answers = {}
    for word, translate in questions.items():
        user_translate = input(f"введите перевод для слова {word} :")
        if user_translate == translate:
            print(f"верно")
        else:
            print(f"неверно переводится как {translate}")
        answers[word] = user_translate == translate
    return answers


def get_result(answers: dict):
    result = len([key for key, value in answers.items() if value])

    return __ranks[result]


# нормально ли вообще так делать чтобы исключения функцию засовывать
# в целом для меня выглядит приемлимо
# обычно я исключения не делаю
# но тут работа с файлами поэтому
# фиг его знает какой файл придет
def read_file_with_user_input(path_file):
    python_data = {}
    try:
        with open(path_file, "r", encoding="utf-8") as f:
            json_data = f.read()
            python_data = json.loads(json_data)

    except FileNotFoundError:
        print("файл не найден")

    except JSONDecodeError:
        print("неверный формат или файл пуст")

    return python_data


def write_stats(user_name, level, result):
    with open(fr"user_statisks\statistics{user_name}.json", "w", encoding="utf-8") as file:
        stats = {"Name": user_name,
                 "words_translated_user": level,
                 "resultUser": result,
                 }
        user_stats = json.dumps(stats, ensure_ascii=False, indent=4)
        file.write(user_stats)
    print("данные записаны")
