from django.urls import path
from . import views

urlpatterns = [
    path('register-shop/', views.CreateSeller.as_view(), name='create_seller'),
    path('bank-details/', views.BankInfoView.as_view(), name='bank_details'),
    path('main/', views.SellerHomeView.as_view(), name='seller_home'),
    path('profile/', views.SellerProfileView.as_view(), name='seller_profile'),
    path('orders/', views.SellerOrdersView.as_view(), name='seller_orders'),
    path('payment/<str:order_id>/', views.SellerPaymentView.as_view(), name='seller_payment'),
    path('order-update/', views.update_order_status, name='update_order_status'),
]
