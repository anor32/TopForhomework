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
