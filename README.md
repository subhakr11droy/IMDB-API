# IMDB-API
A RESTful API service created for movies (something similar to IMDB)

# Requirements
Following are the requirements:
* Python version >= 3.8
* Django 3.2
* Also refer to requirements.txt

# Installation
1. clone desired directory with git clone https://github.com/divinedeveloper/imdb-task.git
2. Create virtual environment
3. pip3 install -r requirements.txt
4. Navigate to folder
5. Run migrations
    * python3 manage.py makemigrations
    * python3 manage.py migrate
6. Populate data from JSON dump
    * python3 manage.py load_data
7. Run the server
    *python3 manage.py runserver

# Functionalities

| Title | API Endpoints |
| --- | --- |
| View all Movies | /api/movies/ |
| View All Genres | /api/genres/ |
| Single movie detail | /api/movie/{id} |
| Search by movie | /api/movies?search={movie-name} |
| Search by genre | /api/movies?search={genre-name} |
| Search by field | /api/movies?search={director-name} |
| Search with multi-field | /api/movies?search={movie-name},{director-name},{genre-name},... |
| Search with Pagination | /api/movies?search=<movie-name>&limit=<#> |

# How to scale the application?
Since, it completely depends on the scenario and requirements and a lot of factors are to be considered before coming up with an approach

Following can be done to scale the application, looking at the current requirements
