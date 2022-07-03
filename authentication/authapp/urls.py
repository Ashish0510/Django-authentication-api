from django.urls import path
from authapp import views


urlpatterns = [
    path('register/',  views.UserRegistrationView.as_view(),name='register'),
    path('login/',  views.UserLoginView.as_view(),name='login'),
    path('profile/',  views.UserProfileView.as_view(),name='profile'),
    path('change/',  views.UserPaschangeView.as_view(),name='change'),
    path('send-reset-password-email/',  views.SendEmailView.as_view(),name='resetpasswordemail'),
    path('reset-password/<uid>/<token>/',  views.UserResetPasswordView.as_view(),name='resetpassword'),

    
]