import requests, json


def dispatch(num, msg):
    r = requests.post('https://rest.nexmo.com/sms/json',
                      data={"to": num,
                            "from": "46769436405",
                            "text": msg,
                            "api_key": json.load(open('secret.json'))["nexmo-key"],
                            "api_secret": json.load(open('secret.json'))["nexmo-secret"],
                            }, timeout=5)
    return r.text


def mass(nums, msg):
    s = requests.session()

    for i in nums:
        r = s.post('https://rest.nexmo.com/sms/json',
                   data={"to": i,
                         "from": "46769436405",
                         "text": msg,
                         "api_key": json.load(open('secret.json'))["nexmo-key"],
                         "api_secret": json.load(open('secret.json'))["nexmo-secret"],
                         }, timeout=5)
        print(r.text)
