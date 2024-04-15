import requests
from sms_logic import SMSLogic
import time

client_number = "+917978622820"


def fetch_data():
    url = 'http://192.168.192.117/sendtext'
    response = requests.get(url)
    data = response.text.strip()  # Strip any leading or trailing whitespace
    # Convert the text data to an integer
    try:
        value = int(data)
        print(f"AQI: {value}")
    except ValueError:
        print("Error: Data is not a valid integer")
        value = None
    return value


sms = SMSLogic()
while True:
    aqi = fetch_data()
    if aqi is not None:
        if aqi > 250:
            sms.send_message(message="Attention! Air quality alert! AQI has exceeded 100. Take precautions and stay "
                                     "indoors if possible. Protect your health with AirGuard Alert",
                             receiverNumber=client_number
                             )
            time.sleep(1000)