from django.urls import path
from . views import Registerview

app_name = 'account'

urlpatterns = [
    path('register/',Registerview.as_view(),name='user_register'),
]