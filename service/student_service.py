from model.student import Student

class StudentService:

    def get_all_students_dict(self):
        students = []
        students.append({"identification":"363763763",
                         "gender":1,"salary":22020202,
                         "job":True,"name":"Carlos Loaiza"})
        students.append({"identification": "363766667",
                         "gender": 2, "salary": 0,
                         "job": False, "name": "Valentina Hurtado"})
        students.append({"identification": "233t6363",
                         "gender": 1, "salary": 10000000,
                         "job": True, "name": "Kevin Sánchez"})
        return students

    def get_all_students(self):
        students = []
        students.append(Student("363763763",1,22020202,
                         True,"Carlos Loaiza"))
        students.append(Student("363766667",2, 0,False, "Valentina Hurtado"))
        students.append(Student("233t6363",1,10000000,True, "Kevin Sánchez"))
        return students