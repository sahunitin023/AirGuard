from twilio.rest import Client
from constants import account_sid, auth_token, twilio_number


class SMSLogic:

    def __init__(self):
        self._client = Client(account_sid, auth_token)

    def send_message(self, message, receiverNumber):
        message_response = self._client.messages.create(
            from_=twilio_number,
            body=message,
            to=receiverNumber
        )

        return message_response
