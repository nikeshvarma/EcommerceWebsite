from django.urls import path
from . import views

urlpatterns = [
    path('profile/update', views.ProfileView.as_view(), name='profile_page'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('update-cart/', views.updatecart),
    path('check-cart/', views.check_item_in_cart),
    path('session-cart/', views.update_session_cart),
]
