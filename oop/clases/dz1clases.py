class Vehicle:
    def __init__(self, mark, mileage):
        self.mark = mark
        self.mileage = mileage

    def get_vehicle_type(self, wheels):
        tips = ["моноколесо", "мотоцикл", "трицикл", "автомобиль"]
        if 4 > wheels - 1 >= 0:
            return f"Это {tips[wheels - 1]} марки {self.mark}"
        return "я незнаю  таких тс"

    def get_vehicle_advice(self):
        advice = {
            (0, 5000): f"Неплохо {self.mark}, можно брать.",
            (5001, 10000): f"{self.mark}, надо внимательно проверить.",
            (10001, 15000): f"{self.mark}, надо провести полную диагностику.",
            (15001, float('inf')): f"{self.mark}, лучше не покупать."
        }
        for range_limit, message in advice.items():
            if range_limit[0] <= self.mileage <= range_limit[1]:
                return message

        return "отрицательного пробега быть не может"


mono = Vehicle("bmv", 10)
moto = Vehicle("audi", 1000)
trycicle = Vehicle("land", 10000)
auto = Vehicle("ferari", 43230)
print(mono.get_vehicle_type(1))
print(mono.get_vehicle_advice())

print(moto.get_vehicle_type(2))
print(moto.get_vehicle_advice())

print(trycicle.get_vehicle_type(3))
print(trycicle.get_vehicle_advice())

print(auto.get_vehicle_type(4))
print(auto.get_vehicle_advice())
