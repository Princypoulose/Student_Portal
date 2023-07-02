from flask_restful import Resource
from app.utils import response_util
from app.logic.Student import LoginLogic


class StudentLogin(Resource):

    def post(self):
        try:
            login_logic = LoginLogic()
            login_logic.login()
            tokens = login_logic.generate_token()
            response = {
                "message": "Student logged in successfully!!!"
            }
            response.update(tokens)
            return response_util.success(response)
        except Exception as e:
            return response_util.error(str(e))
