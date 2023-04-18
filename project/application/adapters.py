from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render

class MyAccountAdapter(DefaultAccountAdapter):
    def confirm_email(self, request, email_address):
        """
        Marks the email address as confirmed on the db
        """
        email_address.verified = True
        email_address.set_as_primary(conditional=True)
        email_address.save()
        mail = EmailMessage(
            body="Thanks for verification!",
            from_email=self.get_from_email(),
            to=[email_address]
        )
        mail.send()

    def send_mail(self, template_prefix, email, context):
        msg = self.render_mail(template_prefix, email, context)
        # msg.send()
        email = EmailMessage(
            subject=msg.subject,
            body=msg.body,
            from_email=msg.from_email,
            to=msg.to
        )
        email.send()


    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        # Call the parent class's save_user method
        user = super().save_user(request, user, form, commit=False)

        try:
            user.save()
        except IntegrityError as e:
            # check if the error is due to the email already existing in the database
            if 'account_emailaddress_email_key' in str(e):
                # return custom error message to user
                return HttpResponse("You are already have this one")
            else:
                # handle other types of IntegrityErrors
                pass
        return user


class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        """
        Invoked just after a user successfully authenticates via a social
        provider, but before the login is actually processed.
        """
        # Get the email address associated with the social account
        email = sociallogin.account.extra_data.get('email')

        # If the email address is already registered, we'll simply log the
        # user in rather than raising an error
        if email and self.email_exists(email):
            # Assign the existing user to the social account
            user = get_user_model().objects.get(email=email)
            sociallogin.connect(request, user)

    def email_exists(self, email):
        """
        Returns True if an email address is already registered in the database.
        """
        User = get_user_model()
        return User.objects.filter(email=email).exists()

