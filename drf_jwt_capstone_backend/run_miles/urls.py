from django.urls import path
from run_miles import views

urlpatterns = [
    path('', views.get_all_runmiles)
]