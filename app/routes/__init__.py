from flask_restful import Api
from app.components import HelloWorld, Student, StudentLogin, Course, Fees, Graduate


def initialize_routes(api: Api):
    api.add_resource(HelloWorld, '/')
    api.add_resource(Student, '/student')
    api.add_resource(StudentLogin, '/student/login')
    api.add_resource(Course, '/course')
    api.add_resource(Fees, '/fees')
    api.add_resource(Graduate, '/graduate')