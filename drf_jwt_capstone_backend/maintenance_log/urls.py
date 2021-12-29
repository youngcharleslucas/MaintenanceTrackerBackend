from django.urls import path
from maintenance_log import views

urlpatterns = [
    path('all/', views.get_all_maintenance_log),
    path('vehicle/<str:id>/', views.get_log_for_vehicle)
]