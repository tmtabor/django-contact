from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from contact.utils import email_user
from django.conf import settings
from . import client


def contact(request):
    subject = request.GET.get('subject')
    recaptcha = client.displayhtml(settings.RECAPTCHA_PUBLIC_KEY, {}, {})

    if subject is None:
        subject = ""
    return render(request, 'contact.html', {'subject': subject, 'captcha': recaptcha})


def submit(request):
    subject = request.POST["subject"]
    message = request.POST["message"]
    email = request.POST["email"]

    recaptcha_response = client.submit(
        request.POST.get('g-recaptcha-response'),
        settings.RECAPTCHA_PRIVATE_KEY,
        request.META['REMOTE_ADDR'], )

    if recaptcha_response.is_valid:
        # email_user(settings.CONTACT_EMAIL, settings.CONTACT_PREFIX + subject, message, email)
        messages.success(request, "Your message has been sent.")

        return HttpResponseRedirect(settings.CONTACT_FORWARD)
    else:
        messages.error(request, "Invalid reCAPTCHA submission.")
        return HttpResponseRedirect(settings.CONTACT_FORWARD)
