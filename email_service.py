from flask import Flask, request, jsonify
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

class EmailService:
    def send_email(self, user_email, pdf_path):
        # Add your email configuration here
        email_address = "ananthu@gmail.com"
        email_password = "ananthupass"

        msg = EmailMessage()
        msg.set_content("Please find attached your bank statement.")
        msg['Subject'] = "Bank Statement"
        msg['From'] = email_address
        msg['To'] = user_email

        with open(pdf_path, 'rb') as file:
            msg.add_attachment(file.read(), maintype='application', subtype='pdf', filename='bank_statement.pdf')

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(email_address, email_password)
            server.send_message(msg)

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    user_email = data.get('user_email')
    pdf_path = data.get('pdf_path')

    EmailService().send_email(user_email, pdf_path)

    return jsonify({'message': 'Email sent successfully'})

if __name__ == '__main__':
    app.run(port=5003)
