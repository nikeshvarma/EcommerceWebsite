from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    path('/contact-us', views.ContactView.as_view(), name='contact_us'),
    path('/about-us', views.AboutView.as_view(), name='about_us'),
]
