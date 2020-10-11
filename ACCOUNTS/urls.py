from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login_page'),
    path('signup/', views.SignUp.as_view(), name='signup_page'),
    path('logout/', views.logout_user, name='logout_page'),
    path('check-email/', views.check_register_email, name='checkEmail')
]
