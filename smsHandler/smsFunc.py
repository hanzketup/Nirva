from .lang import langresolver as lr

def smsSorter(sms):  #handle and sort valid sms requests

    if sms.is_user:
        kw = sms.kw
        if kw[0] == '*':
            Handlecommand(sms)

        else:
            return sms.respond(lr.msg('nf', sms.lang))
    else:
        return sms.respond(lr.msg('nu', sms.lang))


def Handlecommand(smsobj):
    pass