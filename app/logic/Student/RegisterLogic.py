import json

from app.services import ExternalApi


class RegisterLogic:
    def __init__(self):
        self.reg_no = None

    def create_finance_account(self):
        form_data = {
            "studentId": self.reg_no
        }
        api = ExternalApi('http://127.0.0.1:8081/accounts/', content_type='application/json')
        api.data = form_data
        response = api.fetch('post')

    def create_library_account(self):
        form_data = {
            "studentId": self.reg_no
        }
        api = ExternalApi('http://127.0.0.1:80/api/register', content_type='application/json')
        api.data = form_data
        response = api.fetch('post')

