from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    path('<str:product_type>/details/<str:name>/<str:id>/info', views.ProductDetailView.as_view(), name='product_detail_page'),
    path('categories', views.CategoryView.as_view(), name='shop_by_category'),
    path('search', views.SearchView.as_view(), name='search_result'),
    path('checkout', views.CheckOutView.as_view(), name='checkout_page'),
    path('about-us', views.AboutView.as_view(), name='about_us'),
]
