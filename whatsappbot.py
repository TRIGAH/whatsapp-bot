import requests
import aiohttp
import asyncio
import json
import os
from dotenv import load_dotenv
load_dotenv()

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
VERSION = os.getenv('VERSION')
PHONE_NUMBER_ID=os.getenv('PHONE_NUMBER_ID')
WHATSAPP_ACCOUNT_ID=os.getenv('WHATSAPP_ACCOUNT_ID')
RECIPIENT = os.getenv('RECIPIENT')

url=f"https://graph.facebook.com/v19.0/{WHATSAPP_ACCOUNT_ID}/message_templates?field=name"
headers={
    'Authorization':f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json'
}

response=requests.get(url,headers=headers)

TEMPLATE_NAME=response.json()['data'][0]['name']
print(f"------{TEMPLATE_NAME}-----")

async def send_message(data):
  headers = {
    "Content-type": "application/json",
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    }
  
  async with aiohttp.ClientSession() as session:
    url = 'https://graph.facebook.com' + f"/{VERSION}/{PHONE_NUMBER_ID}/messages"
    try:
      async with session.post(url, data=data, headers=headers) as response:
        if response.status == 200:
          print("Status:", response.status)
          print("Content-type:", response.headers['content-type'])

          html = await response.text()
          print("Body:", html)
        else:
          print(response.status)        
          print(response)        
    except aiohttp.ClientConnectorError as e:
      print('Connection Error', str(e))


def get_templated_message_input(recipient,template_name):
  return json.dumps({ 
    "messaging_product":"whatsapp",
    "to":recipient,
    "type":"template",
    "template": { 
        "name":template_name,
        "language": { "code":"en" }
         }
})


async def main():
    data = get_templated_message_input(RECIPIENT,TEMPLATE_NAME)
    await send_message(data)   


asyncio.run(main())   