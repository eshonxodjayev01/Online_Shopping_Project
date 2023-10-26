from django.urls import path
from . import views

urlpatterns = [
    path('expired/', views.expired, name='expired'),
    path('shop_sell_total/', views.shop_sell_total, name='shop_sell_total'),
    path('best_selling_product/', views.best_selling_product, name='best_selling_product'),
    path('categories/', views.categoriy, name='categoriy'),
    path('categories/<uuid:pk>/', views.categoriy_id, name='categoriy_id'),
    path('categories/create/', views.categoriy_created, name='categoriy_create'),
    path('categories/<uuid:pk>/update/', views.categoriy_update, name='categoriy_update'),
    path('categories/<uuid:pk>/delete/', views.categoriy_delete, name='categoriy_delete'),
    path('products/', views.Product, name='Product'),
    path('products/<uuid:pk>/', views.Product_id, name='Product_id'),
    path('products/create/', views.Product_created, name='Product_create'),
    path('products/<uuid:pk>/update/', views.Product_update, name='Product_update'),
    path('products/<uuid:pk>/delete/', views.Product_delete, name='Product_delete'),
]
