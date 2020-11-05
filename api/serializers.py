from rest_framework import serializers
from api.models import Movie, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']


class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
