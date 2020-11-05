from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name="api-overview"),
    path('movies/', views.movie_list, name="movie-list"),
    path('genres/', views.genre_list, name="genre-list"),
]
