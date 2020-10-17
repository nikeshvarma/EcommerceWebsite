from django.urls import path

from LAPTOP import views

urlpatterns = [
    path('list/', views.LaptopHomeView.as_view(), name='laptop_home'),
]
