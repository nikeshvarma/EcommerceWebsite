from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.BookHomeView.as_view(), name='book_home'),
]
