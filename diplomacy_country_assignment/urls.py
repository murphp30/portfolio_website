from django.urls import path
from diplomacy_country_assignment import views

app_name = "diplomacy_country_assignment"
urlpatterns = [
    path("", views.assignment, name="assignment"),
    path("success/", views.success, name="success"),
]