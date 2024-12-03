class Teacher:
    def __init__(self, name, last_name, education, expirence):
        self.__name = name
        self.__last_name = last_name
        self.__education = education
        self.__expirence = expirence

    @property
    def name(self):
        return self.__name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def education(self):
        return self.__education

    @property
    def expirence(self):
        return self.__expirence

    @expirence.setter
    def expirence(self, expirence):
        self.__expirence = expirence

    def get_teacher_data(self):
        return f"{self.__name} {self.__last_name} Образование {self.__education}, опыт работы {self.__expirence}"

    def add_mark(self, student, mark):
        return f"{self.__name} {self.__last_name} поставил оценку {mark} студенту {student}"

    def remove_mark(self, student, mark):
        return f"{self.__name} {self.__last_name} удалил оценку {mark} студенту {student}"

    def give_a_consultation(self, classwork):
        return f"{self.__name} {self.__last_name} провел коснультацию в классе {classwork}"


programer = Teacher("Дмитрий", "Сульжиц", 'МГУ', "10 лет")
print(programer.get_teacher_data())
print(programer.add_mark("Андрей Никанов","12"))
print(programer.remove_mark("Иван Иванов","10"))
print(programer.give_a_consultation("python426"))

class DisciplineTeacher(Teacher):
    def __init__(self, name, last_name, education, expirence, discipline, job_title):
        super().__init__(self, name, last_name, education, expirence)
        self.__discipline = discipline
        self.__job_title = job_title

    @property
    def discipline(self):
        return self.__discipline
    @property
    def job_title(self):
        return self.__job_title
    @job_title.setter
    def job_title(self,new_job):
         self.__job_title = new_job



programer2 = DisciplineTeacher("Волтер","Вайт","Высшее","3 года","Химия","учитель")
