class Powerunit :
    def __init__(self,power):
        self.power = power
    def add_power(self,power):
        self.power +=power
        if power == 220:
            print("Напряжения достаточно")
            return True
        else:
            return False
class Motherboard(Powerunit):
    def __init__(self,chipset):
        self.chipset = chipset
    def distibute_voltage(self,power):
        self.power



class MainProcessor:
    def __init__(self,hertz,cores,switch):
        self.hertz = hertz
        self.cores = cores


    def activate_turbo(self,switch = "off"):
        if switch == "off":

            return False
        else:
            print("Турбо режим активен")
            return True
class Ram:
    def __init__(self,v,ram_gertz):
        self.v = v
        self.ram_getz = ram_gertz

    def load_dates(self,dates):
        self.dates = dates
    def unload_dates(self):
        self.dates = ""

class SSD:
    def __init__(self,ssd_capacity):
      self.ssd_capacity = ssd_capacity
      self.ssd_data = []
    def save_data(self,data):
      self.ssd_data.append(data)
    def delete_data(self,data):
        self.ssd_data.remove(data)
class VideoCard:
    def __init__(self,model_card,memory_card):
       self.model_card = model_card
       self.memory_card=memory_card
    def display_image(self):
        print("изображение")
