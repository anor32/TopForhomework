class Vehicle :
    def __init__(self,mark,mileage):
        self.mark = mark
        self.mileage = mileage
    def get_vehicle_type(self,wheels):
       tips= ["моноколесо","мотоцикл","трицикл","автомобиль"]
       if 4>wheels-1>=0:
           return f"Это {tips[wheels-1]} марки {self.mark}"
       return "я незнаю  таких тс"


mot = Vehicle("bmv",100)
print(mot.get_vehicle_type(1))