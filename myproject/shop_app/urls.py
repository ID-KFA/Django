from django.urls import path
from . import views

urlpatterns = [
    path('orders/<int:customer_id>/', views.all_orders, name='all_orders'),
    path('client/<int:client_id>/', views.client_orders, name='client_orders'),


]