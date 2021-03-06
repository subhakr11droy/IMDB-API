# Generated by Django 3.1.3 on 2020-11-05 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popularity', models.FloatField()),
                ('director', models.CharField(db_index=True, max_length=50)),
                ('imdb_score', models.FloatField()),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('genre', models.ManyToManyField(to='api.Genre')),
            ],
        ),
    ]
