from django.urls import path
from maintenance_item import views

urlpatterns = [
    path('all/', views.get_all_maintenance_items),
]