from bson import ObjectId
from daba.Mongo import collection


class Numbering:
    numbering = collection("Numbering")

    def __init__(self, _id=None, number=None):
        
        self._id = _id
        self.number = number

    def save(self):
        if self._id is None:  
            data = {
                'number': self.number
            }
            # Remove None values from data
            data = {k: v for k, v in data.items() if v is not None}
            result = self.numbering.put(data)
            self._id = result.inserted_id  # Update the ID with the newly generated ID.
        else:  # This user already exists, so update it.
            data = {
                'number': self.number
            }
            # Remove None values from data
            data = {k: v for k, v in data.items() if v is not None}
            self.numbering.set({'_id': ObjectId(self._id)}, data)
        return self._id

    def get(self, query):
        return self.numbering.get(query)

    def getOne(self, query):
        return self.numbering.getOne(query)

    def update(self, query, new_data):
        return self.numbering.set(query, new_data)

    def delete(self, query):
        return self.numbering.deleteOne(query)

    def count(self, query):
        return self.numbering.count(query)
    
    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        if value is not None:
            self.__id = ObjectId(value)
        else:
            self.__id = None
