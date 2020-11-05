from django.core.management.base import BaseCommand
from api.models import Movie, Genre
import json


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            with open('imdb_dump.json') as file_obj:
                list_of_movies = json.loads(file_obj.read())

                # generator to generate all the movie from JSON string
                movies_generator = (movie for movie in list_of_movies)
                movie_obj, no_of_rows = {}, 0

                # querying every movie in movie_generator and inserting in db
                for movie in movies_generator:
                    movie_obj['popularity'] = movie.get('99popularity')
                    movie_obj['director'] = movie.get('director')
                    movie_obj['imdb_score'] = movie.get('imdb_score')
                    movie_obj['name'] = movie.get('name')

                    movie_, __ = Movie.objects.get_or_create(**movie_obj)
                    genre_list = movie.get('genre')

                    # populate one or more genres for a movie
                    for genre in genre_list:
                        genre_title, __ = Genre.objects.get_or_create(name=genre.strip())
                        movie_.genre.add(genre_title)
                    movie_.save()
                    no_of_rows += 1

                self.stdout.write(self.style.SUCCESS(f'Data loaded successfully!\n{no_of_rows} record(s) inserted'))
                return

        except IOError as e:
            self.stdout.write(self.style.ERROR(f'File not found. {e}'))
            return
