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
            "Ssd": 20}

    def distibute_voltage(self, *obj_components):

        if self.check_power():
            for component in obj_components:
                name = type(component).__name__

                if name in self.required_power:
                    component.power = self.required_power[name]
                else:
                    print(f"не найден компонент {name}")
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


class Ssd:
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
ssd = Ssd(512)  # 512GB SSD
videocard = VideoCard("NVIDIA GeForce RTX 3060", 12)  # GPU

computer = Computer(power_supply, motherboard, cpu, ram, ssd, videocard)


# computer.power_on()
#
# motherboard.distibute_voltage(cpu,ssd,videocard,ram)
#
# ram.load_data("Program Data 1")
# ram.load_data("Program Data 2")
# ram.unload_data("Program Data 1")
#
#
# ssd.save_data("File 1")
# ssd.save_data("File 2")
# ssd.delete_data("File 1")
#
#
# cpu.activate_turbo("OFF")
#
# videocard.display_image()

# так как в задании не указано должен ли я все эти методы вызывать через класс компьютера я их вызвал от их экземпляров
# в задании сказано реализовать через наследование и композицию я не понял что конкретно имеется ввиду
# что я должен в одном задании использовать инаследование и композицию или что я должен  сделать это задание дважды
# я выбрал второй вариант
# опять же в задании не указано должен ли я во всех классах использовать наследование или достаточно только одного компьютера
# я выберу тоже второй вариант я просто класс компьютер перепишу






class Сomputerinh(Motherboard, Cpu, Ram, Ssd, VideoCard):
    def __init__(self, power, chipset, hertz, cores, size_ram, ram_hertz, ssd_capacity, model_card, memory_card):

        Powerunit.__init__(self, power)
        Motherboard.__init__(self, chipset,power)
        Cpu.__init__(self, hertz, cores)
        Ram.__init__(self, size_ram, ram_hertz)
        Ssd.__init__(self, ssd_capacity)
        VideoCard.__init__(self, model_card, memory_card)
        self.power = power
        self.chipset = chipset
        self.hertz = hertz
        self.cores = cores
        self.size_ram = size_ram
        self.ram_hertz = ram_hertz
        self.ssd_capacity = ssd_capacity
        self.model_card = model_card
        self.memory_card = memory_card

    def power_on(self):
        if self.check_power():
            self.display_image()


comput = Сomputerinh (
    600,  'X570',
    3.8,8,
    16,3200,
    512,'RTX 3060'
    ,6)


print(comput.check_power())
comput.distibute_voltage(cpu,ram,ssd)
comput.activate_turbo("On")
comput.save_data("file1")
comput.delete_data("file1")

comput.load_data("b")
print(comput.dates)
comput.unload_data("b")
print(comput.dates)
comput.display_image()

comput.power_on()

# как понял так и сделал в задаче не особо описано как это должно выглядить сделал на свое усмотрение