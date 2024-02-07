import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
print(account_sid)
print(auth_token)
client = Client(account_sid, auth_token)

message = client.messages.create(
         from_='whatsapp:+14348305405',
         body='Hi, Joe! Thanks for placing an order with us. We’ll let you know once your order has been processed and delivered. Your order number is O12235234. Thanks',
         to='whatsapp:+2348172829491'
     )

print(message.sid)
