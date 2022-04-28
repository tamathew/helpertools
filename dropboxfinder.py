from telethon import TelegramClient, events
import datetime
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
from twilio.rest import Client

def whatsapp_send(msg,tonum):
    os.environ['TWILIO_ACCOUNT_SID'] = 'ACb0***********************04bf099' 
    os.environ['TWILIO_AUTH_TOKEN'] = 'cc2******************************e52' 
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    print("Sending whatsapp message")
    message_thomas = client.messages.create(
                                body=msg,
                                from_='whatsapp:+141********6',
                                to=f'whatsapp:{tonum}'
                            )




api_id="1#######9"
api_hash="4###################6"



user_input_channel = "https://t.me/H1B_H4_Visa_Dropbox_slots"

client = TelegramClient('botfrommilcreek', api_id, api_hash)
@client.on(events.NewMessage(chats=user_input_channel))
async def my_event_handler(event):
    msg=event.text
    msg_length=len(msg)
    if event.photo or  ( msg_length<=20 and 'avail' in msg.lower() and not('not avail' in  msg.lower()) or ('booked' in msg.lower() and msg_length<=20) or ('open' in msg.lower() and  msg_length<=20)) :
        print("******* Screenshot *******")
        filename='telegram_dropbox_screenshot.jpg'
        await client.download_media(event.media,"images/"+filename)
        if event.photo:
            msg='<image or screenshot>'
        whatsapp_send("Appointment may be available : "+msg,'+19727413431')
        # whatsapp_send("Appointment may be available : "+msg,'+14253624845')#Arun
        #send_email()
    datesuffix=datetime.datetime.now().strftime("%Y-%m-%d")
    current_time=datetime.datetime.now().isoformat()
    print(current_time+'|'+msg)
    f = open(f"logs/dropbox_{datesuffix}.txt", "a")
    row = current_time+'|'+msg+'\n'
    f.write(row)
    f.close()
try:    
    print("Starting to listen to telegram")
    client.start()
    client.run_until_disconnected()
except Exception as e:
    print(f"Exception : {str(e)}")
