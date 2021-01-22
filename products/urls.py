from django.urls import path

from . import views

app_name='products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='list'),
    #path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('<slug:product_slug>/', views.ProductDetailSlugView.as_view(), name='detail'),
]
