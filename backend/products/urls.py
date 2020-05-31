from django.urls import path
from .views import ProductDetailView, ProductListView

app_name = 'products'

urlpatterns = [
    # products views
    path('', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

]
