from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name="api-overview"),
    # path('movies/', views.movie_list, name="movie-list"),
    # path('genres/', views.genre_list, name="genre-list"),
    path('movie/<str:id>', views.movie_details, name='movie-details'),
    path('movies/', views.MovieListView.as_view(), name="movie-list"),
    path('genres/', views.GenreListView.as_view(), name="genre-list"),
]
