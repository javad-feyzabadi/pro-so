from django.urls import path
from . views import UserRegisterview,UserLoginView,UserLogoutView,UserProfileView

app_name = 'account'

urlpatterns = [
    path('register/',UserRegisterview.as_view(),name='user_register'),
    path('login/',UserLoginView.as_view(),name='user_login'),
    path('logout/',UserLogoutView.as_view(),name='user_logout'),
    path('profile/<int:user_id>/',UserProfileView.as_view(),name='user_profile')
]