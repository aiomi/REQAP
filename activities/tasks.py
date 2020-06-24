from django.conf import settings
from django.contrib.auth.models import Group
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from users.models import User
from activities.models import Transcript
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


@app.task
def send_transcript_alert_staff(user_pk, domain, trans_pk):
    """
    Alerts academic user that a transcript request was paid so he/she can
    attend to that request
    """

    user = User.objects.get(pk=user_pk)

    context = {
        'username': user.username,
        'first_name':user.first_name,
        'last_name':user.last_name,
        'domain':domain,
        'trans_pk': trans_pk
        }
    group = Group.objects.get(name='Academic Office')
    staffs = group.staff_set.all()
    for staff in staffs:
        context['staff']=staff.user.username
        
        send_email.delay(
            f"Transcript Request",
            'transcripts/staff_transcript_request.html',
            to_email =[staff.user.email],
            username=user.username,
            context=context
        )
    return True

@app.task
def send_transcript_alert_user(status, user_pk):
    """
    Alerts who made a transcript request that it's that it has been forwarded
    """
    if status:
        user = User.objects.get(pk=user_pk)
        context = {
            'first_name': user.first_name,
            }
        send_email.delay(
            f"Transcript Request Sent",
            'transcripts/user_transcript_request.html',
            to_email =[user.email],
            username=user.username,
            context=context
        )
        return True

@app.task
def transcript_mail_flow(user_pk, *args):
    domain =args[0]
    trans_pk = args[1]
    chain = send_transcript_alert_staff.s(user_pk, domain, trans_pk)\
        | send_transcript_alert_user.s(user_pk)
    chain()