from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.filters import SearchFilter, OrderingFilter

from .serializers import MovieSerializer, GenreSerializer
from .models import Movie, Genre


# Create your views here.

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'View All Movies': '/api/movies/',
        'View All Genres': '/api/genres/',
        'SingleMo detail': '/api/movie/<id>',
        'Search by movie': '/api/movies?search=<movie-name>',
        'Search by genre': '/api/movies?search=<genre-name>',
        'Search by field': '/api/movies?search=<director-name>',
        'Search with Pagination ': '/api/movies?search=<movie-name>&limit=<#>',
        'Search with multi-field': '/api/movies?search=<movie-name>,<director-name>,<genre-name>,...',

    }
    return Response(api_urls)


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def genre_list(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_details(request, id):
    movies = Movie.objects.get(pk=id)
    serializer = MovieSerializer(movies, many=False)
    return Response(serializer.data)


'''
    Using default search filter makes all this CRUD operations trivial
    API using search filter implementation
'''


class MovieListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['name', 'director', 'popularity', 'imdb_score', 'genre__name']


class GenreListView(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [OrderingFilter]
    search_fields = ['name']
