from twilio.rest import Client
import os
import importlib.util
# Get the absolute path to the constants.py file
constants_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'shared_resources', 'constants.py'))

# Load the constants.py module from the file path
spec = importlib.util.spec_from_file_location('constants', constants_path)
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)


def client_initialization() -> Client:
    """
    Initializes a client for Twilio.
    """
    twilio_sid = os.environ.get(c.twilio_sid_env_var)
    twilio_auth_token = os.environ.get(c.twilio_auth_token_env_var)
    client = Client(twilio_sid, twilio_auth_token)
    return client


def text(client, msg: str, destination_phone_number: str) -> str:
    """
    Sends a text using Twilio.

    Inputs:
    client:  The Twilio client initialized by client_initialization.
    msg:  The message you want to send.
    destination_phone_number:  The phone number you want to send the message to.

    Outputs:
    The SID provided by the client upon sending the message.
    """
    message = client.messages.create(
        body=msg,
        from_=c.twilio_source_phone_number,
        to=destination_phone_number
    )
    return message.sid


if __name__=="__main__":
    client = client_initialization()
    text(client=client, msg="Dodona is learning to speak", destination_phone_number="+1 224 478 5394")

