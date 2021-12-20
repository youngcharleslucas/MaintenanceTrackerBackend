from django.urls import path
from run_miles import views

urlpatterns = [
    path('all/', views.get_all_runmiles)
]