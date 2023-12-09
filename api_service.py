from flask import Flask, request, jsonify

app = Flask(__name__)

pdf_service_url = 'http://localhost:5002/generate-pdf'
email_service_url = 'http://localhost:5003/send-email'

@app.route('/generate-statement', methods=['POST'])
def generate_statement():
    data = request.get_json()
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    user_email = data.get('user_email')

    # Trigger PDF Generation Service
    pdf_response = requests.post(pdf_service_url, json={'start_date': start_date, 'end_date': end_date, 'user_email': user_email})
    pdf_result = pdf_response.json()

    if 'pdf_path' in pdf_result:
        # Trigger Email Service
        email_response = requests.post(email_service_url, json={'user_email': user_email, 'pdf_path': pdf_result['pdf_path']})
        email_result = email_response.json()

        return jsonify({'message': 'Bank statement generated and sent successfully'})

    return jsonify({'message': 'Failed to generate bank statement'})

if __name__ == '__main__':
    app.run(port=5001)