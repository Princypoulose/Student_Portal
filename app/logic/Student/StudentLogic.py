from app.models import Student, Numbering
from app.utils import str_util, request_util, pswd_util, mongo_util, dt_util


class StudentLogic:
    def __init__(self):
        self.reg_no = None
        self.user_fields = ["first_name", "last_name", "phone", "email", "date_of_birth", "gender", "is_active",
                            "is_graduated", "student_id"]
        self.student = Student()
        self._id = None

    def register(self):
        number = self.get_new_number()

        self.reg_no = 'c' + str(number).zfill(5)
        self.student.student_id = self.reg_no
        self.student.first_name = request_util.json_data('first_name')
        self.student.last_name = request_util.json_data('last_name')
        self.student.phone = request_util.json_data('phone')
        self.student.email = request_util.json_data('email', str, request_util.email)
        self.student.date_of_birth = dt_util.parse_date(request_util.json_data('date_of_birth'))
        self.student.gender = request_util.json_data('gender')
        self.student.is_active = True
        self.student.is_graduated = False
        self.student.password = pswd_util.hash_password(request_util.json_data('password'))

        self.student.save()

        self._id = self.student._id
        return self._id

    @classmethod
    def get_new_number(cls):
        number_model = Numbering()
        number_table = number_model.numbering.getAfterCount({}, "number")
        if number_table:
            number = number_table.get("number")
        else:
            number = 1
            number_model.number = 1
            number_model.save()
        return number

    def get_student_data(self):
        data = self.student.getOne({"_id": mongo_util.ObjectId(self._id)})
        response = {k: mongo_util.process_value(v) for k, v in data.items() if k in self.user_fields}
        return response

    def update(self):
        data = {k: request_util.json_data(k) for k in self.user_fields if request_util.json_data(k)}
        self.student.update({"_id": mongo_util.ObjectId(self._id)}, data)

    def delete(self):
        self.student.delete({"_id": mongo_util.ObjectId(self._id)})

    def check_graduate(self):
        data = self.get_student_data()
        if data.get("is_graduated"):
            return {
                "message": "Student has already graduated",
                "can_graduate": False
            }
        self.reg_no = data.get('student_id')
        return True

    def graduate(self):
        self.student.update({"_id": mongo_util.ObjectId(self._id)}, {"is_graduated": True})
        return True
