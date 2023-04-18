from django.urls import path

from . import views
from .views import ProductListView, ProductDetailView, search

urlpatterns = [
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('books/', ProductListView.as_view(), name="product_list"),
    path('books/<int:pk>/', ProductDetailView.as_view(), name="product_detail"),
    path('search/', search, name="search")
]
