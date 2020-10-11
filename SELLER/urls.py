from django.urls import path
from . import views

urlpatterns = [
    path('register-shop/', views.CreateSeller.as_view(), name='create_seller'),
    path('main/', views.SellerHomeView.as_view(), name='seller_home'),
    path('profile/', views.SellerProfileView.as_view(), name='seller_profile'),
    path('orders/', views.SellerOrdersView.as_view(), name='seller_orders'),
    path('payment/', views.SellerPaymentView.as_view(), name='seller_payment'),
]
