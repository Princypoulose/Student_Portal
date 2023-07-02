from app.logic.Student import StudentLogic, LoginLogic, RegisterLogic
from flask_restful import Resource
from app.utils import response_util
from app.services.UserService import protected, user

student = StudentLogic()


class Student(Resource):

    @protected
    def get(self):
        try:
            student._id = user.Id
            student_data = student.get_student_data()
            return response_util.success(student_data)
        except Exception as e:
            return response_util.error(str(e))

    def post(self):
        try:
            student_id = student.register()
            register_logic = RegisterLogic()
            register_logic.reg_no = student.reg_no
            register_logic.create_finance_account()
            register_logic.create_library_account()
            login_logic = LoginLogic()
            login_logic.user_id = student_id
            tokens = login_logic.generate_token()
            response = {
                "message": "Student registered successfully!!!"
            }
            response.update(tokens)
            return response_util.success(response)
        except Exception as e:
            return response_util.error(str(e))

    @protected
    def put(self):
        try:
            student._id = user.Id
            student.update()
            return response_util.success({"message": "Student data updated successfully"})
        except Exception as e:
            return response_util.error(str(e))

    @protected
    def delete(self):
        try:
            student._id = user.Id
            student.delete()
            return response_util.success({"message": "User deleted successfully"})
        except Exception as e:
            return response_util.error(str(e))
