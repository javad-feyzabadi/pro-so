from django.urls import path
from . views import UserRegisterview,UserLoginView

app_name = 'account'

urlpatterns = [
    path('register/',UserRegisterview.as_view(),name='user_register'),
    path('login/',UserLoginView.as_view(),name='user_login'),
]