from flask import Flask, render_template, jsonify, request
from twilio.twiml.messaging_response import MessagingResponse
import processor


app = Flask(__name__)

app.config['SECRET_KEY'] = 'enter-a-very-secretive-key-3479373'


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())



# @app.route('/chatbot', methods=["GET", "POST"])
# def chatbotResponse():

#     if request.method == 'POST':
#         the_question = request.form['question']

#         response = processor.chatbot_response(the_question)

#     return jsonify({"response": response })


@app.route('/chatbot', methods=["POST"])
def chatbotResponse():
    the_question = request.values.get('Body', '').lower()
    try:
        response = processor.chatbot_response(the_question)
        print(response)  
        resp = MessagingResponse()
        msg = resp.message()
        msg.body(response)
        return str(resp)
    except:
        response = processor.chatbot_response(the_question)
        print(response)  
        resp = MessagingResponse()
        msg = resp.message()
        msg.body("I am sorry, I cannot understand your message")
        return str(resp)
        
if __name__ == '__main__':
    #app.run(host='0.0.0.0', port='8888', debug=True)
    app.run()