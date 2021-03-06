from django.urls import path
from vehicle import views

urlpatterns = [
    path('all/', views.get_all_vehicles),
    # path('', views.user_vehicles),
    path('create/', views.create_vehicle),
    path('get_vehicle/<str:id>/', views.get_vehicle),
    path('update_miles/<str:id>/', views.update_miles),
    path('nongarage_vehicle/<str:id>/', views.get_nongarage_vehicle),
]