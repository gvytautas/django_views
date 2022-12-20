from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('show_services/', views.ShowServicesView.as_view(), name='show_services'),
    path('show_orders/', views.ShowOrdersView.as_view(), name='show_orders'),
    path('show_order_detail/<order_id>/', views.ShowOrderDetailView.as_view(), name='show_order_detail'),
]
