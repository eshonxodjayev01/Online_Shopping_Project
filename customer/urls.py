from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/<int:pk>/', views.customer_id, name='customer_id'),
    path('customers/create/', views.customer_created, name='customer_created'),
    path('customers/<int:pk>/update/', views.customer_update, name='customer_update'),
    path('customers/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
]
