from django.urls import path
from maintenance_log import views

urlpatterns = [
    path('all/', views.get_all_maintenance_log),
    path('all/incomplete/', views.get_all_maintenance_log_incomplete),
    path('vehicle/log/<str:id>/', views.get_log_for_vehicle),
    path('vehicle/maintenance_item/<str:id>/', views.get_maintenance_item_for_vehicle),
    path('vehicle/maintenance_item_log/<str:id>/', views.get_maintenance_log),
    path('vehicle/maintenance_item_log/incomplete/<str:id>/', views.get_incomplete_logs),
    path('vehicle/maintenance_item_log/complete/<str:id>/', views.get_update_complete_true), 
    path('log/new/', views.post_new_log),  
]