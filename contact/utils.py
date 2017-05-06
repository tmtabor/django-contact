from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.contrib.auth.models import User
from django.core.mail import send_mail
import sys

__author__ = 'Thorin Tabor'


PY2 = sys.version_info[0] == 2
if PY2:
    text_type = unicode
    from urllib2 import Request, urlopen
    from urllib import urlencode
else:
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode

    text_type = str


def want_bytes(s, encoding='utf-8', errors='strict'):
    if isinstance(s, text_type):
        s = s.encode(encoding, errors)
    return s


def email_user(user, subject, message, sent_by=DEFAULT_FROM_EMAIL):
    if isinstance(user, User):
        to_email = user.email
    else:
        to_email = user
    send_mail(subject, message, sent_by, [to_email])
