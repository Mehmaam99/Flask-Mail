from flask import Flask,render_template,request
from flask_mail import Mail, Message
from flask_restful import Resource,Api

app= Flask(__name__)


api=Api(app)

app.config.update(
MAIL_SERVER='smtp.gmail.com',
MAIL_PORT='465',
MAIL_USERNAME='drfitness999@gmail.com',
MAIL_PASSWORD='DoctorFitness999',
MAIL_USE_TLS= False,
MAIL_USE_SSL= True
)

mail= Mail(app)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/send_message', methods=['POST', 'GET'])

def send_message():
    if request.method == 'POST':
        email = request.form['email']
        subject = request.form['subject']
        msg = request.form['msg']

        message=Message(subject=subject, sender=email, recipients=["drfitness999@gmail.com"])
        message.body =email +"\n" + msg

        mail.send(message)
        return "Message sent successfully."

        


    # if request.method == 'POST':
    #     msg=Message(request.form.get("Subject"),sender="muhammadmehmaam@gmail.com" ,recipients=["drfitness999@gmail.com"])
    #     msg.body= "Cool email bro"
    #     mail.send(msg)
    #     return render_template('result.html',result='success!')
    # else:
    #     return render_template('result.html',result='Failure!')

if __name__=='__main__':
    app.run(debug = True)

