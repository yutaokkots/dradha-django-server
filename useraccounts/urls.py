"""Module providing URL patterns for useraccounts-related API views"""
from django.urls import path, include
from useraccounts.views import GithubLoginView
# 'api/auth/'
urlpatterns = [
    # path("", Class.as_view(), name="getuser"),
    path("github/", GithubLoginView.as_view(), name="github"),
]
