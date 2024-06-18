from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "accounts"

urlpatterns = [
    
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    
    # reset password django.contrib.auth
    path(
        "password_reset/",
        views.CustomPasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.CustomPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.CustomPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
