from django.urls import path
from vehicle_main_part import views

urlpatterns = [
    path('all/', views.get_all_vehicle_main_parts),
]