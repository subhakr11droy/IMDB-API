from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieSerializer, GenreSerializer
from .models import Movie, Genre


# Create your views here.

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': '/movies/',
        'List': '/genres/',
        'Detail_view': '/task-list/',
        'Detail_view1': '/task-list/',
        'Detail_view2': '/task-list/',
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
