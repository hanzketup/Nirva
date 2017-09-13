import json
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

"""

Lang code reference:

nu = not user (user not in db)
nf = not found


"""


def msg(key, lang="eng"): #Resolve an automtic message from a language file

    with open(os.path.join(__location__, lang + '.json')) as data_file:
        data = json.load(data_file)

    try:
        return data[key]
    except:
        return ("lang err: ", key)