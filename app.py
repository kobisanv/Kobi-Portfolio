from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587  # Use port 587 for TLS
app.config['MAIL_USERNAME'] = 'kobisan.vinotharupan@gmail.com'
app.config['MAIL_PASSWORD'] = 'wcxu fcbu gabm ryqm'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


def send_email(email, subject, message):
    msg = Message(
        subject,
        sender=email,
        recipients=['kobisan.vinotharupan@gmail.com']
    )

    msg.body = message

    try:
        mail.send(msg)
        return render_template('emailsuccess.html')
    except Exception as e:
        return render_template('emailnotsuccess.html') + f'Error: {str(e)}'


@app.route('/')
def index():
    return render_template('email.html')


@app.route('/send_email', methods=['POST'])
def send_email_route():
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    result = send_email(email, subject, message)
    return result


if __name__ == '__main__':
    app.run(debug=True)
