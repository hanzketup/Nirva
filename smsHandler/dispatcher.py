import requests


def dispatch(num, msg):
    r = requests.post('https://rest.nexmo.com/sms/json',
                      data={"to": num,
                            "from": "46769436405",
                            "text": msg,
                            "api_key": "76e3575b",
                            "api_secret": "2ca2ac5f9a6520ff", }, timeout=5)
    return r.text