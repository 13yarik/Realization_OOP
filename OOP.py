class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and lecturer in course.lecturers:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            print("Ошибка: лектор не преподает данный курс или студент не записан на данный курс")

    def __str__(self):
        avg_grade_student = sum(sum(grades) / len(grades) for grades in self.grades.values()) / len(self.grades) if self.grades else "у студента нет оценок"
        courses_student = [course.name for course in self.courses_in_progress]
        finished_courses_student = [course.name for course in self.finished_courses]

        courses_in_progress_error = ', '.join(courses_student) if courses_student else 'нет курсов в процессе изучения'
        finished_courses_error = ', '.join(finished_courses_student) if finished_courses_student else 'нет завершенных курсов'
    
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {round(avg_grade_student, 1)}\n"
                f"Курсы в процессе изучения: {courses_in_progress_error}\n"
                f"Завершенные курсы: {finished_courses_error}"
                )
    
    def __lt__(self, student):
        if not isinstance(student, Student):
            print("Ошибка: Это не студент")
            return       
        avg_grade_student_1 = sum(sum(grades) / len(grades) for grades in self.grades.values()) / len(self.grades) 
        avg_grade_student_2 = sum(sum(grades) / len(grades) for grades in student.grades.values()) / len(student.grades) 
        return avg_grade_student_1 < avg_grade_student_2

    def __eq__(self, student):
        if not isinstance(student, Student):
            print("Ошибка: Это не студент")
            return 
        avg_grade_student_1 = sum(sum(grades) / len(grades) for grades in self.grades.values()) / len(self.grades) 
        avg_grade_student_2 = sum(sum(grades) / len(grades) for grades in student.grades.values()) / len(student.grades)
        return avg_grade_student_1 == avg_grade_student_2

       
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
    
    def __str__(self):
        num_courses = len(self.grades)
        if num_courses > 0:
            total_grade = 0
            course_grades = ""
            for course, grades in self.grades.items():
                course_average = sum(grades) / len(grades)
                total_grade += course_average
                course_grades += f"{course.name}: {course_average}\n"
            avg_grade_lecturer = total_grade / num_courses
        else:
            avg_grade_lecturer = 0
            course_grades = "Нет оценок"
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {round(avg_grade_lecturer, 1)}"
                )
    
    def __lt__(self, lecturer):
        if not isinstance(lecturer, Lecturer):
            print("Ошибка: Это не лектор")
            return       
        avg_grade_lecturer_1 = sum(sum(grades) / len(grades) for grades in self.grades.values()) / len(self.grades) 
        avg_grade_lecturer_2 = sum(sum(grades) / len(grades) for grades in lecturer.grades.values()) / len(lecturer.grades) 
        return avg_grade_lecturer_1 < avg_grade_lecturer_2

    def __eq__(self, lecturer):
        if not isinstance(lecturer, Lecturer):
            print("Ошибка: Это не лектор")
            return 
        avg_grade_lecturer_1 = sum(sum(grades) / len(grades) for grades in self.grades.values()) / len(self.grades) 
        avg_grade_lecturer_2 = sum(sum(grades) / len(grades) for grades in lecturer.grades.values()) / len(lecturer.grades)
        return avg_grade_lecturer_1 == avg_grade_lecturer_2
    
    
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
        
    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return (f"Имя:{self.name}\n"
                f"Фамилия:{self.surname}"
                )


class Course:
    def __init__(self, name, lecturers):
        self.name = name
        self.lecturers = lecturers


def get_avg_grades_students(students, course_name):
    grades = []
    for student in students:
        for course in student.courses_in_progress:
            if course.name == course_name:
                grades.extend(student.grades[course])
    if grades:
        return sum(grades) / len(grades)
    else:
        return None
    
def get_avg_grades_lecturers(lecturers, course_name):
    grades = []
    for lecturer in lecturers:
        for course in lecturer.courses_attached:
            if course.name == course_name:
                grades.extend(lecturer.grades[course])
    if grades:
        return sum(grades) / len(grades)
    else:
        return None



student_1 = Student("Ruoy", "Eman1", "мужской")
student_2 = Student("Ruoy", "Eman2", "мужской")
student_3 = Student("Ruoy", "Eman3", "женский")

lecturer_1 = Lecturer("Some", "Boddy1")
lecturer_2 = Lecturer("Some", "Boddy2")
lecturer_3 = Lecturer("Some", "Boddy3")

reviewer_1 = Reviewer("Some", "Boddy1")
reviewer_2 = Reviewer("Some", "Boddy2")
reviewer_3 = Reviewer("Some", "Boddy3")

course_1 = Course("Python", [lecturer_1])
course_2 = Course("Git", [lecturer_2])
course_3 = Course("Python ООП", [lecturer_3])

student_1.courses_in_progress.append(course_1)
student_1.courses_in_progress.append(course_2)
student_1.courses_in_progress.append(course_3)

student_2.courses_in_progress.append(course_1)
student_2.courses_in_progress.append(course_2)
student_2.courses_in_progress.append(course_3)

student_3.courses_in_progress.append(course_1)
student_3.courses_in_progress.append(course_2)
student_3.courses_in_progress.append(course_3)

lecturer_1.courses_attached.append(course_1)
lecturer_2.courses_attached.append(course_2)
lecturer_3.courses_attached.append(course_3)

reviewer_1.courses_attached.append(course_1)
reviewer_2.courses_attached.append(course_2)
reviewer_3.courses_attached.append(course_3)

student_1.rate_lecture(lecturer_1, course_1, 10)
student_1.rate_lecture(lecturer_2, course_2, 7)
student_1.rate_lecture(lecturer_3, course_3, 9)

student_2.rate_lecture(lecturer_1, course_1, 8)
student_2.rate_lecture(lecturer_2, course_2, 10)
student_2.rate_lecture(lecturer_3, course_3, 6)

student_3.rate_lecture(lecturer_1, course_1, 10)
student_3.rate_lecture(lecturer_2, course_2, 7)
student_3.rate_lecture(lecturer_3, course_3, 10)

reviewer_1.rate_student(student_1, course_1, 8)
reviewer_1.rate_student(student_2, course_1, 9)
reviewer_1.rate_student(student_3, course_1, 10)

reviewer_2.rate_student(student_1, course_2, 10)
reviewer_2.rate_student(student_2, course_2, 8)
reviewer_2.rate_student(student_3, course_2, 7)

reviewer_3.rate_student(student_1, course_3, 9)
reviewer_3.rate_student(student_2, course_3, 8)
reviewer_3.rate_student(student_3, course_3, 8)


# print(student_1)
# print(lecturer_1)
# print(reviewer_1)

# print(student_3 == student_2)
# print(lecturer_1 < lecturer_2)

# avg_grade_student = get_avg_grades_students([student_1, student_2, student_3], course_2.name)
# print(avg_grade_student)
 
# avg_grade_lecturers = get_avg_grades_lecturers([lecturer_1, lecturer_2, lecturer_3], course_2.name)
# print(avg_grade_lecturers)


