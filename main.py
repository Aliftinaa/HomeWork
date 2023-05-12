
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_lcr(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rate(self):
        sum_rate = 1
        len_rate = 1
        for course in self.grades.values():
            sum_rate += sum(course)
            len_rate += len(course)
        av_rate = round(sum_rate / len_rate, 2)
        return av_rate

    def av_rate_courses(self, course):
        course_sum = 0
        course_len = 0
        for lesson in self.grades.keys():
            if lesson == course:
                course_sum += sum(self.grades[course])
                course_len += len(self.grades[course])
            average_rate = round(course_sum / course_len, 2)
            return average_rate

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.average_rate()}\n' \
               f'Курсы в процессе изучения:{", ".join(self.courses_in_progress)}\n ' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}\n'



    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Преподователей и студентов между собой не сравнивают!")
            return
        return self.average_rate() < other.average_rate()
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []




class Lecturer(Mentor):
    def __init__(self, name, surname):
      super().__init__(name, surname)
      self.grades = {}

    def average_rate(self):
        sum_rate = 0
        len_rate = 0
        for course in self.grades.values():
            sum_rate += sum(course)
            len_rate += len(course)
        average_rate = round(sum_rate/len_rate, 2)
        return average_rate

    def av_rate_courses(self, course):
        course_sum = 0
        course_len = 0
        for lesson in self.grades.keys():
            if lesson == course:
                course_sum += sum(self.grades[course])
                course_len += len(self.grades[course])
            average_rate = round(course_sum / course_len, 2)
            return average_rate

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rate()}\n"

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Преподователей и студентов между собой не сравнивают!")
            return
        return self.average_rate() < other.average_rate()




class Reviewer(Mentor):
    def __init__(self, name, surname):
      super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n"



student1 = Student('Maria','Dvebashni','woman')
student1.courses_in_progress = ['Python']
student1.finished_courses = ["Java"]

student2 = Student('Alyya', 'Fufuza', 'woman')
student2.courses_in_progress = ['Pyton']
student2.finished_courses = ['Go']


'''lectors'''
some_lecturer1 = Lecturer('Nikita', 'Mokrov')
some_lecturer1.courses_attached += ['Python']

some_lecturer2 = Lecturer('Alona', 'Trahein')
some_lecturer2.courses_attached += ['Python']


'''reviwers'''
reviewer1 = Reviewer('Marina', 'Yanetakaya')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Oleg', 'Skorohod')
reviewer2.courses_attached += ['Python']

'''lecturer ratings'''
student1.rate_lcr(some_lecturer1 ,'Python', 10 )
student1.rate_lcr(some_lecturer2 ,'Python', 8)

student2.rate_lcr(some_lecturer1 ,'Python', 10)
student2.rate_lcr(some_lecturer2 ,'Python', 6)

'''student grades'''
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student2, 'Python', 10)

reviewer2.rate_hw(student1, 'Python', 10)
reviewer2.rate_hw(student2, 'Python', 7)



student_list = [student1, student2]
lectors_list = [some_lecturer1, some_lecturer2]

import gc

print('Список проверяющих')
for object in gc.get_objects():
    if isinstance(object, Reviewer):
        print(object)

print('Список лекторов')
for object in gc.get_objects():
    if isinstance(object, Lecturer):
        print(object)

print('Список студентов')
for object in gc.get_objects():
    if isinstance(object, Student):
        print(object)



print('Сравнение людей по средним оценкам:')
print('Студент 1 < Студент 2', student1 < student2)
print('Лектор 1 > лектор 2', some_lecturer1 > some_lecturer2)
print('Студент 1 > лектор 1', student1  > some_lecturer1)
print()
def average_rate_courses(course, student_list ):
    sum_ = 0
    quantity_ = 0
    for student in student_list:
        for course in student.grades:
            student_sum = student.av_rate_courses(course)
            sum_ += student_sum
            quantity_ += 1
    average_rate = round(sum_ / quantity_, 2)
    return average_rate

print('Подсчет средней оценки у студентов: ', average_rate_courses('Python', student_list) )

print('Подсчет средней оценки у лекторов: ', average_rate_courses('Python', lectors_list) )


