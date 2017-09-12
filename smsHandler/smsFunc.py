import requests



def smsSorter(smsobj):  #handle and sort valid sms requests

    kw = smsobj.kw
    if kw[0] == '*':
        Handlecommand(smsobj)

    else:
        return msg


def dispatch(num,msg): #dispatch a message to the api
    r = requests.post('https://rest.nexmo.com/sms/json',
                      data={"to": to, "from": "46769436405",
                            "text": txt, "api_key": "76e3575b",
                            "api_secret": "2ca2ac5f9a6520ff", })
    return r.response