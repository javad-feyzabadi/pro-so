from django.urls import path
from . views import (UserRegisterview,UserLoginView,
                     UserLogoutView,UserProfileView,
                     UserPasswordResetView,
                     UserPasswordResetDoneView,UserPasswordResetConfirmView,
                     UserPasswordResetCompleteView,
)

app_name = 'account'

urlpatterns = [
    path('register/',UserRegisterview.as_view(),name='user_register'),
    path('login/',UserLoginView.as_view(),name='user_login'),
    path('logout/',UserLogoutView.as_view(),name='user_logout'),
    path('profile/<int:user_id>/',UserProfileView.as_view(),name='user_profile'),
    path('reset/' ,UserPasswordResetView.as_view(),name='reset_password'),
    path('reset/done/',UserPasswordResetDoneView.as_view(),name='password_reset_done'),
    path('confirm/<uidb64>/<token>',UserPasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('confirm/complete/',UserPasswordResetCompleteView.as_view(),name='password_reset_complete'),



]