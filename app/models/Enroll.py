from bson import ObjectId
from daba.Mongo import collection


class Enroll:
    enroll = collection("Enroll")

    def __init__(self, _id=None, course_id=None, student_id=None, enrolled_date=None):
        
        self._id = _id
        self.course_id = course_id
        self.student_id = student_id
        self.enrolled_date = enrolled_date

    def save(self):
        if self._id is None:  
            data = {
                'course_id': self.course_id,
                'student_id': self.student_id,
                'enrolled_date': self.enrolled_date
            }
            # Remove None values from data
            data = {k: v for k, v in data.items() if v is not None}
            result = self.enroll.put(data)
            self._id = result.inserted_id  # Update the ID with the newly generated ID.
        else:  # This user already exists, so update it.
            data = {
                'course_id': self.course_id,
                'student_id': self.student_id,
                'enrolled_date': self.enrolled_date
            }
            # Remove None values from data
            data = {k: v for k, v in data.items() if v is not None}
            self.enroll.set({'_id': ObjectId(self._id)}, data)
        return self._id

    def get(self, query):
        return self.enroll.get(query)

    def getOne(self, query):
        return self.enroll.getOne(query)

    def update(self, query, new_data):
        return self.enroll.set(query, new_data)

    def delete(self, query):
        return self.enroll.deleteOne(query)

    def count(self, query):
        return self.enroll.count(query)
    
    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        if value is not None:
            self.__id = ObjectId(value)
        else:
            self.__id = None

    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        if value is not None:
            self._course_id = ObjectId(value)
        else:
            self._course_id = None

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        if value is not None:
            self._student_id = ObjectId(value)
        else:
            self._student_id = None
