import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

# Load environment variables and Twilio client
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
twilio_client = Client(account_sid, auth_token)

call = twilio_client.calls.create(
    # Trick to load XML without a webserver
    twiml = """<Response><Say voice="man">1! 2! 3! Hello friend. It's working!</Say></Response>""",
    # url = "http://demo.twilio.com/docs/voice.xml",
    to = "+12345678",
    from_ = "+87654321"
)

print(call.sid)