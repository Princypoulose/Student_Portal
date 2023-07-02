from app.models import Courses, Enroll
from app.utils import request_util, mongo_util, dt_util
from app.logic.Fees import FeesLogic


class CourseLogic:
    def __init__(self):
        self.course = Courses()
        self._id = None
        self.course_fields = [
            "_id",
            "course_id",
            "course_name",
            "fees"
        ]
        self.student_id = None

    def add_course(self):
        self.course.course_id = request_util.json_data('course_id')
        self.course.course_name = request_util.json_data('course_name')
        self.course.fees = request_util.json_data('fees', int, request_util.number)
        self.course.term = request_util.json_data('term', int, request_util.number)
        self.course.status = 1
        self.course.save()

    def all_courses(self):
        data = mongo_util.process_cursor(self.course.get({}))
        result = []
        for d in data['data']:
            result.append({k: mongo_util.process_value(d[k]) for k in self.course_fields})
        response = {
            "count": data['count'],
            "data": result
        }
        return response

    def enroll(self):
        self._id = request_util.json_data('courseId')
        result = self.course.getOne({"_id": mongo_util.ObjectId(self._id)})
        enroll = Enroll()
        enroll.student_id = mongo_util.ObjectId(self.student_id)
        enroll.course_id = mongo_util.ObjectId(self._id)
        enroll.enrolled_date = dt_util.get_current_time()
        enroll.save()
        fees = result.get('fees')
        fees_logic = FeesLogic()
        fees_logic.student_id = self.student_id
        fees_logic.fees = fees
        fees_logic.generate_invoice()

