import random
from django.apps import apps

"""

Generates a code and check the db to make sure its unique.
To be used on the Offer 'code' field.

The code is 2 letters and 1 number in this format:

[a-z][a-z][1-9]

"""

letters = 'abcdefghijklmnopqrstuvwxyz'
nums = '123456789'


def get_code():

    excode = new_code()

    if validate_code(excode):
        return excode
    else:
        get_code()


def new_code():
    return random.choice(letters) + random.choice(letters) + random.choice(nums) + random.choice(nums)


def validate_code(excode):
    Offer = apps.get_model('dashBoard', 'Offer')
    q = list(Offer.objects.all())

    for i in q:
        if i.code == excode:
            return False
        else:
            continue

    return True
