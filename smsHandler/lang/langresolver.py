import json
import os
import datetime

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

"""

Lang code reference:

nu = not user (user not in db)
cnf = not found

inr = invalid response

tail = string that generates the tail of every offer message

"""


def msg(key, lang="eng"):  # Resolve an automatic message from a language file

    with open(os.path.join(__location__, lang + '.json')) as data_file:
        data = json.load(data_file)

    try:
        return data[key]
    except:
        return "lang err: ", key


def generate_tail(code, unit, time):  # Generate the tail of the message (respond __ {quantity} before date)
    time = time.date()
    s = msg('tail')
    return s.format(code, unit, time)