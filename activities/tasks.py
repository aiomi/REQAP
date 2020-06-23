from django.conf import settings
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from users.models import User
from main.celery import app

@app.task(bind=True)
def send_email(self, subject, email_template, to_email=None, from_email=settings.DEFAULT_FROM_EMAIL, context=None, username=None):
    if not context:
        if username:
            context = {'user': User.objects.get(username=username)}
    html_msg = render_to_string(f'emails/{email_template}', context)
    txt_msg = strip_tags(html_msg)
    message = EmailMultiAlternatives(subject=subject, body=txt_msg, from_email=from_email, to=to_email)
    message.attach_alternative(html_msg, "text/html")
    try:
        message.send()
    except Exception as exc:
        raise self.retry(exc=exc)

