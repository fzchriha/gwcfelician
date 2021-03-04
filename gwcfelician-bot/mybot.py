from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
import emoji
import os 
app = Flask(__name__)
account = os.environ.get("ACCOUNT_SID")
token = os.environ.get("TOKEN")
client = Client(account, token)
@app.route("/")
def Hello():
    return "Hello Girls Who Code"
@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message.""" 
    
    # Fetch the message
    msg = request.form.get('Body')
    phone_number = request.form.get('From')
    resp = MessagingResponse()      
    
   
    # Write your Story
    if 'hello' in msg.lower():
        resp.message("""Hi I am Fatima Zahra's Bot how can I help you?
        Not sure.. send *menu* to get started""")
        return str(resp)
    
    if 'menu' in msg.lower():
        resp.message("""Okaay, welcome to FatimaZ world!
        So to know my academic journey (rollercoaster) send *school*
        Want to know what I do for fun send *fun* (so creative)
        Let's talk professional shall we? send *career*\n""")
        return str(resp)
    if 'school' in msg.lower():
        resp.message("""Oh I'm a sophomore double majoring in CS and Math at Felician University
        (no I can't fix your laptop)
        I have a 4.0 GPA (go me! \N{hugging face})""")
        return str(resp)



if __name__ == "__main__":
    app.run(debug=True)