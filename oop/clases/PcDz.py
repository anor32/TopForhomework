class Powerunit:
    def __init__(self, power):
        self.power = power

    def add_power(self, power):
        self.power += power

    def check_power(self):

        if self.power >= 320:

            return True
        else:

            return False


class Motherboard(Powerunit):
    def __init__(self, chipset, power):
        super().__init__(power)
        self.chipset = chipset
        self.required_power = {
            "VideoCard": 100,
            "Cpu": 60,
            "Ram": 20,
            "SSD": 20}

    def distibute_voltage(self,*obj_components):
        if self.check_power():
            for component in  obj_components:
                name = type(component).__name__

                if name in self.required_power:
                    component.power = self.required_power[name]
                else:
                    print("не найден компонент")
            print("Напряжение распределено")
class Cpu:
    def __init__(self, hertz, cores):
        self.hertz = hertz
        self.cores = cores
        self.power = 0

    def activate_turbo(self, switch="off"):
        if self.power >= 40 and switch == "On":
            self.hertz += 20
            self.power -= 40
            print("Турбо режим активен")
            return True
        print("Турбо режим не активен")
        return False


class Ram:
    def __init__(self, size_ram, ram_gertz):
        self.size_ram = size_ram
        self.ram_getz = ram_gertz
        self.power = 0
        self.dates = []

    def load_data(self, data):
        self.dates.append(data)
        print(f"данные {data} сохранены")

    def unload_data(self, data):
        self.dates.remove(data)
        print(f"данные {data} удалены ")


class SSD:
    def __init__(self, ssd_capacity):
        self.ssd_capacity = ssd_capacity
        self.ssd_data = []

    def save_data(self, data):
        if len(self.ssd_data) < self.ssd_capacity:
            self.ssd_data.append(data)
            print(f"данные{data} сохранены")
        else:
            print("недостаточно места")

    def delete_data(self, data):
        if data in self.ssd_data:
            self.ssd_data.remove(data)
            print("данные удалены")
        else:
            print("нет в базе данных")


class VideoCard:
    def __init__(self, model_card, memory_card):
        self.model_card = model_card
        self.memory_card = memory_card
        self.power = 0

    def display_image(self):
        print("изображение")


class Computer:
    def __init__(self, obj_power_unit, obj_mother_board, obj_cpu, obj_ram, obj_ssd, obj_video_card):
        self.power_unit = obj_power_unit
        self.mother_board = obj_mother_board
        self.cpu = obj_cpu
        self.ram = obj_ram
        self.ssd = obj_ssd
        self.videocard = obj_video_card

    def power_on(self):
        if self.power_unit.check_power():
            self.videocard.display_image()

    def load_data(self, data):
        return self.ram.load_data(data)


power_supply = Powerunit(600)
motherboard = Motherboard("Chipset A", 600)
cpu = Cpu(3.4, 4)
ram = Ram(16, 3200)
ssd = SSD(512)  # 512GB SSD
videocard = VideoCard("NVIDIA GeForce RTX 3060", 12)  # GPU


computer = Computer(power_supply, motherboard, cpu, ram, ssd, videocard)


computer.power_on()

motherboard.distibute_voltage(cpu,ssd,videocard,ram)

ram.load_data("Program Data 1")
ram.load_data("Program Data 2")
ram.unload_data("Program Data 1")


ssd.save_data("File 1")
ssd.save_data("File 2")
ssd.delete_data("File 1")


cpu.activate_turbo("OFF")

videocard.display_image()