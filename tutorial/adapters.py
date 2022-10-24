from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import get_user_model

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
   def pre_social_login(self, request, sociallogin):

    User = get_user_model()

    user = sociallogin.user
    if user.id:
        return
    if not user.email:
        return

    try:
        user = User.objects.get(email=user.email)  # if user exists, connect the account to the existing account and login
        sociallogin.connect(request, user)
    except User.DoesNotExist:
        pass