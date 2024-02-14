from django.urls import path
from pages import views

app_name = "pages"
urlpatterns = [
    path("portfolio_home", views.portfolio_home, name="portfolio"),
    path("", views.index, name="index"),
    path("CV", views.CV, name="CV"),
    path("publications", views.publications, name="publications"),
    path("ireland_pop_density", views.ireland_pop_density, name="ireland_pop_density")
]