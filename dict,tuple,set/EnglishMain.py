import json
from englishUtils import get_user_level, base_program, get_result
python_data={}
try:
    with open("user_inputs.json", "r", encoding="utf-8") as f:
       json_data= f.read()
       python_data =json.loads(json_data)
except (FileNotFoundError):
    print("файл не найден")

    if python_data=={}:
        user_name = input("введите ваше имя")
        dificulty = input("выберете уровень сложности  легкий  средний сложный :").strip().lower()
    else:
        dificulty = python_data["уровень сложности"]
        user_name = python_data["имя пользователя"]

level = get_user_level(dificulty)
answers = base_program(level)
result = get_result(answers)
print("ваш Ранг", result)




with open(f"statistics{user_name}.json","w",encoding="utf-8") as file:
    stats = {"Name": user_name,
             "words_translated_user": level,
             "resultUser": result,
             }
    user_stats = json.dumps(stats, ensure_ascii=False, indent=4)
    file.write(user_stats)

