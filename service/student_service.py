from model.student import Student
import json

class StudentService:
    students = []
    def __init__(self):
        self.students.append(Student("363763763", 1, 22020202,
                                True, "Carlos Loaiza"))
        self.students.append(Student("363766667", 2, 0, False, "Valentina Hurtado"))
        self.students.append(Student("233t6363", 1, 10000000, True, "Kevin Sánchez"))

    def get_all_students(self):
        return self.students

    def get_percentage_students_by_gender(self,gender):
        count =0
        for student in self.students:
            if student.gender == gender:
                count = count +1
        return count/ len(self.students)