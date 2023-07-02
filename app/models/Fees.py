from bson import ObjectId
from daba.Mongo import collection


class Fees:
    fees = collection("Fees")

    def __init__(self, _id=None, student_id=None, fee=None, invoice_id=None, is_paid=None, fees=fees):
        
        self.fee = None
        self._id = _id
        self.student_id = student_id
        self.fees = fees
        self.invoice_id = invoice_id
        self.is_paid = is_paid

    def save(self):
        if self._id is None:  
            data = {
                'student_id': self.student_id,
                'fees': self.fee,
                'invoice_id': self.invoice_id,
                'is_paid': self.is_paid
            }
            # Remove None values from data
            data = {k: v for k, v in data.items() if v is not None}
            result = self.fees.put(data)
            self._id = result.inserted_id  # Update the ID with the newly generated ID.
        else:  # This user already exists, so update it.
            data = {
                'student_id': self.student_id,
                'fees': self.fee,
                'invoice_id': self.invoice_id,
                'is_paid': self.is_paid
            }
            # Remove None values from data
            data = {k: v for k, v in data.items() if v is not None}
            self.fees.set({'_id': ObjectId(self._id)}, data)
        return self._id

    def get(self, query):
        return self.fees.get(query)

    def getOne(self, query):
        return self.fees.getOne(query)

    def update(self, query, new_data):
        return self.fees.set(query, new_data)

    def delete(self, query):
        return self.fees.deleteOne(query)

    def count(self, query):
        return self.fees.count(query)
    
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
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        if value is not None:
            self._student_id = ObjectId(value)
        else:
            self._student_id = None
