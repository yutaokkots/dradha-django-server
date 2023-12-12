from django.shortcuts import render
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.conf import settings

FRONT_END_APP = "http://localhost:3000"

class GithubLoginView(SocialLoginView):
    authentication_classes = [] #disable authetication; override 'allowed origins' in settings.py in production
    adapter_class = GitHubOAuth2Adapter
    callback_url = FRONT_END_APP
    client_class = OAuth2Client
    
    
