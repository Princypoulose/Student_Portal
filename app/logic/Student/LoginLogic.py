from app.models import Student
from app.utils import token_util, request_util, pswd_util
from werkzeug import exceptions


class LoginLogic:
    def __init__(self):
        self.student = Student()
        self.user_id = None

    def login(self):
        student_id = request_util.json_data('student_id')
        data = self.student.getOne({"student_id": student_id})
        if not data:
            raise exceptions.Unauthorized("Student Id does not exist")
        if pswd_util.check_password(request_util.json_data('password'), data.get('password')):
            self.user_id = data.get("_id")
        else:
            raise exceptions.Unauthorized("Password does not match!!!")

    def generate_token(self):
        access_token, refresh_token = token_util.create_tokens(str(self.user_id))
        response = {
            "accessToken": access_token,
            "refreshToken": refresh_token
        }
        return response
