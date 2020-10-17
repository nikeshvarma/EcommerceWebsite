from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.GroceryHomeView.as_view(), name='grocery_home'),
]
