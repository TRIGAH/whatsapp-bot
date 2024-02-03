# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from dotenv import load_dotenv
from flask import Flask, request, Response
load_dotenv() 

app = Flask(__name__)

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='+2348172829491',
                              body='Hello, there!',
                              to='+14155238886'
                          )

print(message.sid)


def greeting_template(name):
    return f"Hello {name}, welcome to the Twilio Bot! How can I assist you today?"

def handle_message(message_body):
    # Parse the incoming message and extract relevant information
    # Here, we assume a simple "name" parameter in the message

    if "name" in message_body.lower():
        user_name = message_body.split(":")[1].strip()
        response = greeting_template(user_name)
    else:
        response = "I'm sorry, I didn't understand that. Please provide your name for a personalized greeting."

    return response



@app.route("/incoming", methods=["POST"])
def incoming():
    message_body = request.form.get("Body", "")
    response = handle_message(message_body)

    message = client.messages.create(
            from_='+2348172829491',
            body='Hello, there!',
            to='+14155238886'
    )

    return Response(status=200)


if __name__ == "__main__":
    app.run(debug=True)


