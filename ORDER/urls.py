from django.urls import path
from . import views

urlpatterns = [
    path('payment-initiate/', views.payment_request, name='payment_initiate'),
    path('payment-validation/', views.payment_status, name='payment_validation'),
]
