from django.urls import path

from signup import views

urlpatterns = [
    path('email/check/', views.SignupEmailCheck, name="signup/email/check"),
    path('email/send/', views.SignupEmailsend, name="signup/email/send"),
    path('auth/check/', views.SignupAuthCheck, name="signup/auth/check"),
    path('auth/send/', views.SignupAuthSend, name="signup/auth/send"),
    path('new/', views.SignupNew, name="signup/new"),
    path('create/', views.SignupCreate, name="signup/create"),
    path('fin/', views.SignupFin, name="signup/fin"),
]
