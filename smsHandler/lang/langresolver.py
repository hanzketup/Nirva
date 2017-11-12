import json
import os
import datetime

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

"""

Lang code reference:

-- format strings --
tail = string that generates the tail of every offer message
confirm = string that generates a confirmation for an 'order'

-- errors --
nu = not user (user not in db)
cnf = not found
nv = no value supplied
inr = invalid response
nact = offer is not active

-- misc --
au = answer updated, when user has answered the offer ones before
arm = your answer has been removed

info = show some basic usage and commands

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

def generate_confirm(code):
    s = msg('confirm')
    return s.format(code)