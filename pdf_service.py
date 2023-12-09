from flask import Flask, request, jsonify
from fpdf import FPDF
import database_service as db
# app = Flask(__name__)

class PDFService:
    def generate_pdf(self, transactions, user_email):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        for _, transaction in transactions.iterrows():
            pdf.cell(200, 10, txt=f"{transaction['date_of_transaction']} - {transaction['amount']}", ln=True, align='L')

        pdf_path = f"{user_email}_bank_statement.pdf"
        pdf.output(pdf_path)
        return pdf_path

# @app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    # data = request.get_json()
    # start_date = data.get('start_date')
    # end_date = data.get('end_date')
    # user_email = data.get('user_email')
     #data = request.get_json()
    start_date = '01/01/2023'
    end_date = '31/12/2023'
    user_email = 'user2@mail.com'
    # Assume DatabaseService is a separate class or module
    transactions = db.DatabaseService().get_transactions(start_date, end_date, user_email)

    pdf_path = PDFService().generate_pdf(transactions, user_email)
    print('PDF path is', pdf_path)
    return
    # return jsonify({'pdf_path': pdf_path})


if __name__ == '__main__':
    # app.run(port=5002)
    generate_pdf()