from app.logic.Fees import FeesLogic
from flask_restful import Resource
from app.utils import response_util
from app.services.UserService import protected, user


class Fees(Resource):

    @protected
    def get(self):
        try:
            fees_logic = FeesLogic()
            fees_logic.student_id = user.Id
            response = fees_logic.get_fees()
            response.update({
                "message": "Fees data of student"
            })
            return response_util.success(response)
        except Exception as e:
            import traceback
            print(traceback.format_exc())
            return response_util.error(str(e))

    @protected
    def put(self):
        try:
            fees_logic = FeesLogic()
            fees_logic.student_id = user.Id
            fees_logic.pay()
            return response_util.success({"message": "Fees paid successfully"})
        except Exception as e:
            return response_util.error(str(e))

    @protected
    def post(self):
        try:
            return response_util.success({"message": "This is the POST method of /fees"})
        except Exception as e:
            return response_util.error(str(e))
