from django.db import models


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=10, db_index=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    popularity = models.FloatField()
    director = models.CharField(max_length=50, db_index=True)
    imdb_score = models.FloatField()
    name = models.CharField(max_length=100, db_index=True)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name
