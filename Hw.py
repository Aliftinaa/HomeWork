from operator import le
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
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_rate()}\nКурсы в процессе изучения:{", ".join(self.courses_in_progress)}\n Завершенные курсы: {", ".join(self.finished_courses)}'

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
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rate()}"

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
        return f"Имя: {self.name} \nФамилия: {self.surname} "



student1 = Student('Maria','Dvebashni','woman')
student1.courses_in_progress = ['Python' , 'Git']
student1.finished_courses = ["Java"]

student2 = Student('Alyya', 'Fufuza', 'woman')
student2.courses_in_progress = ['Pyton','Git']
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
student1.rate_lcr(some_lecturer1 ,'Python', 7 )
student1.rate_lcr(some_lecturer2 ,'Python', 7)

student2.rate_lcr(some_lecturer1 ,'Python', 10)
student2.rate_lcr(some_lecturer2 ,'Python', 5)

'''student grades'''
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student2, 'Python', 9)

reviewer2.rate_hw(student1, 'Python', 8)
reviewer2.rate_hw(student2, 'Python', 7)



student_list = [student1, student2]
reviewer_list = [reviewer1, reviewer2]
lectors_list = [some_lecturer1, some_lecturer2]


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
print(average_rate_courses('Python', student_list))
print(average_rate_courses('Python', lectors_list))
print(student1)
print(student2)
print(some_lecturer1)
print(some_lecturer2)