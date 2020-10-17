from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.FashionHomeView.as_view(), name='fashion_home'),
]
