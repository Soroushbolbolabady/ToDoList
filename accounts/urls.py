from django.urls import path

from .views import login_user, logout_user, signup

app_name = 'accounts'

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("signin/", login_user, name="signin"),
    path('signout/', logout_user, name="signout")
]
