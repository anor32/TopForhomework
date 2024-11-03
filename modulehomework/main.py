import utils
regulars = utils.get_reg_data()
users=[]
dates = ["имя","фамилию","номер телефона в формате +*(***)******* :","ваш email"]

while len(users)<3:
    users_info=[]
    for i in range(len(dates)):
        user_input = input(f"введите {dates[i]}")
        cheking = utils.reg_check(user_input, regulars[i], users_info, users)
        if cheking:
            users_info.append(cheking)
            print("данные приняты")
    users.append(users_info)


print(users)

