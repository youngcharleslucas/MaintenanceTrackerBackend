from django.urls import path
from operator_vehicle import views

urlpatterns = [
    path('', views.get_all_operator_vehicle),
    path('garage/', views.get_operator_vehicle),
]