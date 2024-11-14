

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