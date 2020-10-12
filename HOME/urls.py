from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    path('<str:product_type>/details/<str:name>/<str:id>/info', views.ProductDetailView.as_view(), name='product_detail_page'),
    path('contact-us', views.ContactView.as_view(), name='contact_us'),
    path('about-us', views.AboutView.as_view(), name='about_us'),
]
