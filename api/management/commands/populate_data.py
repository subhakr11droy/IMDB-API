from django.core.management.base import BaseCommand
from api.models import Movie, Genre
from django.conf import settings
import json


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            json_file = f'{settings.BASE_DIR}/imdb_dump.json'

            with open(json_file) as file:
                list_of_movies = json.loads(file.read())
                movies_generator = (movie for movie in list_of_movies)
                movie_obj, no_of_rows = {}, 0

                for movie in movies_generator:
                    movie_obj['popularity'] = movie.get('99popularity')
                    movie_obj['director'] = movie.get('director')
                    movie_obj['imdb_score'] = movie.get('imdb_score')
                    movie_obj['name'] = movie.get('name')

                    movie_, created = Movie.objects.get_or_create(**movie_obj)
                    genres = movie.get('genre')

                    # populate one or more genres for a movie
                    for genre in genres:
                        genre, created = Genre.objects.get_or_create(name=genre.strip())
                        movie_.genre.add(genre)
                    movie_.save()
                    no_of_rows += 1

                self.stdout.write(self.style.SUCCESS(f'Database populated!\n {no_of_rows} record(s) inserted'))
                return

        except IOError as e:
            self.stdout.write(self.style.ERROR(f'File not found. {e}'))
            return
