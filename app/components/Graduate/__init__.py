from flask_restful import Resource
from app.utils import response_util
from app.services.UserService import protected, user
from app.logic.Student import StudentLogic
from app.logic.Fees import FeesLogic


class Graduate(Resource):

    @protected
    def get(self):
        try:
            student_logic = StudentLogic()
            student_logic._id = user.Id
            response = student_logic.check_graduate()
            if not response:
                fees_logic = FeesLogic()
                fees_logic.student_code = student_logic.reg_no
                if not fees_logic.check_graduate_eligible():
                    response = {
                        "message": "Fees not paid. Please pay to graduate",
                        "can_graduate": False
                    }
            response = {
                "message": "Student eligible to graduate",
                "can_graduate": True
            }
            return response_util.success(response)
        except Exception as e:
            import traceback
            print(traceback.format_exc())
            return response_util.error(str(e))

    @protected
    def put(self):
        try:
            student_logic = StudentLogic()
            student_logic._id = user.Id
            student_logic.graduate()
            return response_util.success({"message": "Student graduated successfully"})
        except Exception as e:
            return response_util.error(str(e))
