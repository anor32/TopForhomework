# class Vehicle:
#     def __init__(self, mark, mileage):
#         self.mark = mark
#         self.mileage = mileage
#
#     def get_vehicle_type(self, wheels):
#         tips = ["моноколесо", "мотоцикл", "трицикл", "автомобиль"]
#         if 4 > wheels - 1 >= 0:
#             return f"Это {tips[wheels - 1]} марки {self.mark}"
#         return "я незнаю  таких тс"
#
#     def get_vehicle_advice(self):
#         advice = {
#             (0, 5000): f"Неплохо {self.mark}, можно брать.",
#             (5001, 10000): f"{self.mark}, надо внимательно проверить.",
#             (10001, 15000): f"{self.mark}, надо провести полную диагностику.",
#             (15001, float('inf')): f"{self.mark}, лучше не покупать."
#         }
#         for range_limit, message in advice.items():
#             if range_limit[0] <= self.mileage <= range_limit[1]:
#                 return message
#
#         return "отрицательного пробега быть не может"


# mono = Vehicle("bmv", 10)
# moto = Vehicle("audi", 1000)
# trycicle = Vehicle("land", 10000)
# auto = Vehicle("ferari", 43230)
# print(mono.get_vehicle_type(1))
# print(mono.get_vehicle_advice())
#
# print(moto.get_vehicle_type(2))
# print(moto.get_vehicle_advice())
#
# print(trycicle.get_vehicle_type(3))
# print(trycicle.get_vehicle_advice())
#
# print(auto.get_vehicle_type(4))
# print(auto.get_vehicle_advice())


class Sword:
    def __init__(self,sharp,quality,durability,name_onwer):
        self.sharp= sharp
        self.quality =quality
        self.durability=durability
        self.name_onwer=name_onwer

    def hit(self,target):
        self.durability-=1
        return f"цель {target} получила {self.sharp*10} урона меч и немного поломался"
    def sharpen(self,sharp):
        self.sharp+=sharp
    def show_stats(self):
        print( f"текущий уровень заточки {self.sharp}",
        f"качество Меча {self.quality}",
        f"Текущий показатель прочности {self.durability}",
        f"Хозяин меча {self.name_onwer}",sep="\n")
    def repair_sword(self,points):
        if self.durability+points>100:
            self.durability = 100
            return "меч полностью починен"
        else:
            self.durability =+ points
            return  f"меч починен до {self.durability}"

cladenec = Sword(1,"обычный",100,"иван")
print(cladenec.show_stats())
print(cladenec.hit("monstr"))

cladenec.sharpen(1)
print(cladenec.show_stats())
print(cladenec.hit("monstr"))


# ну я методы немного поменял не так как было написано в документе
# в целом интересная штука эти классы пока не понятно как это использовать
# в серьезном програмировании ну думаю дальше будет яснее