from app.logic.Course import CourseLogic
from flask_restful import Resource
from app.utils import response_util
from app.services.UserService import protected, user


class Course(Resource):

    @protected
    def get(self):
        try:
            course = CourseLogic()
            data = course.all_courses()
            response = {
                "message": "All courses data"
            }
            response.update(data)
            return response_util.success(response)
        except Exception as e:
            return response_util.error(str(e))

    @protected
    def post(self):
        try:
            course = CourseLogic()
            course.add_course()
            return response_util.success({"message": "Course added successfully"})
        except Exception as e:
            return response_util.error(str(e))

    @protected
    def put(self):
        try:
            course = CourseLogic()
            course.student_id = user.Id
            course.enroll()
            return response_util.success({"message": "Student enrolled successfully"})
        except Exception as e:
            import traceback
            print(traceback.format_exc())
            return response_util.error(str(e))

    @protected
    def delete(self):
        try:
            return response_util.success({"message": "This is the DELETE method of /course"})
        except Exception as e:
            return response_util.error(str(e))
