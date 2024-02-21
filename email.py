from flask import Flask, render_template, request
import smtplib as sm
from email.mime.text import MIMEText

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('email.html')


@app.route('/send_email', methods=['POST'])
def send_email():
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    sender_email = email
    sender_password = 'sywi hlwt osbt fuww'
    recipient_email = 'kobisan.vinotharupan@gmail.com'

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    try:
        server = sm.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(recipient_email, sender_password)
        server.sendmail(recipient_email, [sender_email], msg.as_string())
        server.quit()
        return 'Email sent successfully'
    except Exception as e:
        return f'Error: {str(e)}'


if __name__ == '__main__':
    app.run(debug=True)
