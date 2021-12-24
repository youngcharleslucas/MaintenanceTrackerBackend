from django.urls import path
from operator_vehicle import views

urlpatterns = [
    path('', views.get_all_operator_vehicle),
    path('garage/', views.get_operator_vehicle),
    path('drivers/', views.get_vehicle_operator),
    path('add_vehicle/', views.add_vehicle_to_user),
]