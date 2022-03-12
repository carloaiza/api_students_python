from flask import Response, Blueprint, jsonify
from service.student_service import StudentService

app_student = Blueprint("app_student",__name__)

@app_student.route('/student/all')
def get_all_students():
    student_service = StudentService()
    return jsonify(student_service.get_all_students_dict())
