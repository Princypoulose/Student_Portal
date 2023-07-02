from app.models import Fees
from app.services import ExternalApi
from app.logic.Student import StudentLogic
from app.utils import dt_util, mongo_util, request_util


class FeesLogic:
    def __init__(self):
        self.invoice_id = None
        self.fees = None
        self.student_code = None
        self.student_id = None
        self.fees_db = Fees()
        self.fees_field = [
            "_id",
            "invoice_id",
            "fees",
            "is_paid"
        ]

    def generate_invoice(self):
        student_logic = StudentLogic()
        student_logic._id = self.student_id
        student_data = student_logic.get_student_data()
        self.student_code = student_data.get('student_id')
        form_data = {
            "account": {"studentId": self.student_code},
            "amount": self.fees,
            "dueDate": dt_util.format_date(dt_util.add_days(dt_util.get_current_time(), 45)),
            "type": "TUITION_FEES"
        }
        api = ExternalApi('http://127.0.0.1:8081/invoices/', content_type='application/json')
        api.data = form_data
        result = api.fetch('post')
        print(result)
        self.fees_db.student_id = self.student_id
        self.fees_db.fee = self.fees
        self.fees_db.is_paid = False
        self.fees_db.invoice_id = result.get('reference')
        self.fees_db.save()

    def get_fees(self):
        fees_data = mongo_util.process_cursor(self.fees_db.get({"student_id": mongo_util.ObjectId(self.student_id)}))
        result = []
        for f in fees_data.get('data'):
            result.append({k: mongo_util.process_value(f.get(k)) for k in self.fees_field})
        response = {
            "data": result,
            "count": fees_data.get('count')
        }
        return response

    def pay(self):
        self.invoice_id = request_util.json_data('invoiceNo')
        url = f"http://127.0.0.1:8081/invoices/{self.invoice_id}/pay"
        api = ExternalApi(url, content_type='application/json')
        result = api.fetch('put')
        print(result)
        self.fees_db.update({"invoice_id": self.invoice_id}, {"is_paid": True})

    def check_graduate_eligible(self):
        url = f"http://127.0.0.1:8081/accounts/student/{self.student_code}"
        api = ExternalApi(url, content_type='application/json')
        result = api.fetch('get')
        return not result.get('hasOutstandingBalance')

