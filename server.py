import csv
from flask import Flask, render_template, request, redirect
app = Flask(__name__)


# def write_to_file(data):
#     with open('database.txt', mode='a') as db:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = db.write(f'Email: {email}\nSubject: {subject}\nMessage: {message}\n\n')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(db, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to DB'
