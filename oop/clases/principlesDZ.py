class Teacher:
    def __init__(self, name, last_name, education, exp):
        self.name = name
        self.__last_name = last_name
        self.__education = education
        self.__exp = exp

    @property
    def last_name(self):
        return self.__last_name

    @property
    def education(self):
        return self.__education

    @property
    def exp(self):
        return self.__exp

    @exp.setter
    def exp(self, exp):
        self.__exp = exp

    def get_teacher_data(self):
        return f"{self.name} {self.__last_name} Образование {self.__education}, опыт работы {self.__exp}"

    def add_mark(self, student, mark):
        return f"{self.name} {self.__last_name} поставил оценку {mark} студенту {student}"

    def remove_mark(self, student, mark):
        return f"{self.name} {self.__last_name} удалил оценку {mark} студенту {student}"

    def give_a_consultation(self, classwork):
        return f"{self.name} {self.__last_name} провел консультацию в классе {classwork}"

class DisciplineTeacher(Teacher):
    def __init__(self, name, last_name, education, exp, discipline, job_title):
        super().__init__(name, last_name, education, exp)
        self.__discipline = discipline
        self.__job_title = job_title

    @property
    def discipline(self):
        return self.__discipline

    @property
    def job_title(self):
        return self.__job_title

    def get_teacher_data(self):
        return f"{super().get_teacher_data()}, Предмет {self.discipline}, Должность {self.job_title}"

    def add_mark(self, student, mark):
        return f"{super().add_mark(student, mark)} Предмет {self.discipline}"

    def remove_mark(self, student, mark):
        return f"{super().remove_mark(student, mark)} Предмет {self.discipline}"

    def give_a_consultation(self, classwork):
        return f"{super().give_a_consultation(classwork)} Предмет {self.discipline}, Как {self.job_title}"

# Создание объекта Teacher и отладка
programer = Teacher("Дмитрий", "Сульжиц", 'МГУ', "10 лет")
print(programer.get_teacher_data())
print(programer.add_mark("Андрей Никанов", "12"))
print(programer.remove_mark("Иван Иванов", "10"))
print(programer.give_a_consultation("python426"))

# Создание объекта DisciplineTeacher
chemist = DisciplineTeacher("Волтер", "Вайт", "Высшее", "3", "Химия", "учитель")
print(chemist.get_teacher_data())
print(chemist.add_mark("джесси", "5"))
print(chemist.remove_mark("джесси", "5"))
print(chemist.give_a_consultation("сhemistry782"))