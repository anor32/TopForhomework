
words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}
words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}
words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично"
}


words={"легкий":words_easy,
       "средний":words_medium,
       "сложный":words_hard,
}
answers={}
score=0


user_input= input("выберете уровень сложности  легкий  средний сложный :")

for word,translate in words[user_input].items():
    print(f"и так слово {word} перевод  {len(translate)} букв    начинается с {translate[0]}")
    user_answer=input("введите ваш ответ:").lower().strip()
    if user_answer == translate:
        print(f"верно")
        score+=1
    else:
        print(f"неверно переводится как {translate}")
    answers[word]=user_answer == translate


[print("слово",i,"отвечено верно") if k else print("слово",i,"отвечено неверно") for i,k in answers.items()]
print(f"ваш ранг\n{levels[score]}")