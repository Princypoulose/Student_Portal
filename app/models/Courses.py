from bson import ObjectId
from daba.Mongo import collection


class Courses:
    courses = collection("Courses")

    def __init__(self, _id=None, course_id=None, course_name=None, fees=None, status=None, term=None):
        
        self._id = _id
        self.course_id = course_id
        self.course_name = course_name
        self.fees = fees
        self.status = status
        self.term = term

    def save(self):
        if self._id is None:  
            data = {
                'course_id': self.course_id,
                'course_name': self.course_name,
                'fees': self.fees,
                'status': self.status,
                'term': self.term
            }
            # Remove None values from data
            data = {k: v for k, v in data.items() if v is not None}
            result = self.courses.put(data)
            self._id = result.inserted_id  # Update the ID with the newly generated ID.
        else:  # This user already exists, so update it.
            data = {
                'course_id': self.course_id,
                'course_name': self.course_name,
                'fees': self.fees,
                'status': self.status,
                'term': self.term
            }
            # Remove None values from data
            data = {k: v for k, v in data.items() if v is not None}
            self.courses.set({'_id': ObjectId(self._id)}, data)
        return self._id

    def get(self, query):
        return self.courses.get(query)

    def getOne(self, query):
        return self.courses.getOne(query)

    def update(self, query, new_data):
        return self.courses.set(query, new_data)

    def delete(self, query):
        return self.courses.deleteOne(query)

    def count(self, query):
        return self.courses.count(query)
    
    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        if value is not None:
            self.__id = ObjectId(value)
        else:
            self.__id = None
