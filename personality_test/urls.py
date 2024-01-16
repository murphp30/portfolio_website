from django.urls import path
from personality_test import views

app_name = "personality_test"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]