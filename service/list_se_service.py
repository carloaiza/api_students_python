from model.student import Student
from model.list_se import ListSE

class ListSEService:
    cities = ['Manizales', 'Pereira', 'Chinchiná', 'Armenia']

    def __init__(self):
        self.students = ListSE()
        carloaiza = Student("363763763", 1, 5000000,True, "Carlos Loaiza",self.cities[2])
        self.students.add(carloaiza)

    def get_all_students(self):
        return self.students.head
