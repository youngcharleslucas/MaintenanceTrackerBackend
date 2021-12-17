from django.urls import path
from vehicle import views

urlpatterns = [
    path('all/', views.get_all_vehicles),
    path('', views.user_vehicles),
]