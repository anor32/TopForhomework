import re

def get_reg_data():
    regulars = []
    regulars.append(re.compile(r'^[A-Za-zА-Яа-яЁё]+$'))
    regulars.append(re.compile(r'^[A-Za-zА-Яа-яЁё]+$'))
    regulars.append(re.compile(r'^\+\d{1,3}\(\d{1,3}\)\d{7}$'))
    regulars.append(re.compile(r'^[A-Za-z0-9_]+@yandex\.ru$'))

    return regulars


def reg_check(user_data, reg_pattern, users_list, data_to_check=None):
    def check_unique_data(user_data, data_to_check):

        if data_to_check:
            for user_inf in data_to_check:
                if user_data in user_inf[2:]:
                    print("данные уже есть в списке")
                    return False
        return True
    if check_unique_data(user_data, data_to_check) and reg_pattern.match(user_data):
        return user_data

    while True:
        another_check = input("неверные данные введите ещё раз")

        if  bool(reg_pattern.match(another_check)) and check_unique_data(another_check, data_to_check)   :
                return another_check





regulars = get_reg_data()
print()


# я не смог придумать что делать с users_list я незнаю куда его засунуть я решил так
# вообще если бы в реальности нужно было такое сделать я бы не через вложеную функциию делал
# помоему удобнее не через вложенную
# достаточно много времени ушло у меня на это очень долго разбирался
# наконецто началось что то серъезное
# ну я надеюсь что не  я один такой и у других тоже возникли сложности