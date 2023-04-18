# from django.core.mail import EmailMessage
# from django.dispatch import receiver
# from allauth.account.signals import email_confirmed
# from .adapters import MyAccountAdapter
#
# @receiver(email_confirmed)
# def save_user(sender, request, email_address, **kwargs):
#     # Get the user associated with the email address
#     user = email_address.user
#     # Call the custom adapter's save_user method to save the user object
