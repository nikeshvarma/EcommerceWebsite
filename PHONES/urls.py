from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.PhoneHomeView.as_view(), name='phone_home'),
]
