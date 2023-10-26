from django.urls import path
from . import views

urlpatterns = [
    path('shopcards/', views.shopcard_list, name='shopcard_list'),
    path('shopcards/<int:pk>/', views.shopcard_id, name='shopcard_id'),
    path('shopcards/create/', views.shopcard_created, name='shopcard_created'),
    path('shopcards/<int:pk>/update/', views.shopcard_update, name='shopcard_update'),
    path('shopcards/<int:pk>/delete/', views.shopcard_delete, name='shopcard_delete'),
]
