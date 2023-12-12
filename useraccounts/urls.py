"""Module providing URL patterns for useraccounts-related API views"""
from django.urls import path, include
from useraccounts.views import GithubLoginView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from dj_rest_auth.app_settings import api_settings

# api/login/
# api/social/login/
urlpatterns = [
    path("social/github/", GithubLoginView.as_view(), name="github"),
    #path("auth/github/", GithubLoginView.as_view(), name="githubauth"),
    # dj_rest_auth related views.
    path('password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),
    path("auth/login/", LoginView.as_view(), name='rest_login'),
    path('auth/logout/', LogoutView.as_view(), name='rest_logout'),
    path('auth/user/', UserDetailsView.as_view(), name='rest_user_details'),
    path('password/change/', PasswordChangeView.as_view(), name='rest_password_change'),
]

if api_settings.USE_JWT:
    from rest_framework_simplejwt.views import TokenVerifyView
    from dj_rest_auth.jwt_auth import get_refresh_view
    urlpatterns += [
        path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
        path('token/refresh/', get_refresh_view().as_view(), name='token_refresh'),
    ]