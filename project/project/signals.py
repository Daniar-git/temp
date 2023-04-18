from allauth.socialaccount.signals import pre_social_login
from django.dispatch import receiver

@receiver
def save_email_adress(request, user, **kwargs):
    email = request.data.email
    email.save()