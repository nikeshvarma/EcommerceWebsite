from django.urls import path
from . import views

urlpatterns = [
    path('inventory/', views.InventoryListView.as_view(), name='inventory_page'),
    path('list-product/', views.ListProductView.as_view(), name='list_product'),
    path('<str:id>/update/', views.UpdateProductView.as_view(), name='update_listing'),
    path('<str:id>/delete/', views.ProductDeleteView.as_view(), name='delete_listing'),
    path('<str:category>/<str:id>/update-info/', views.ProductDetailUpdateView.as_view(), name='update_phone_details'),
]
