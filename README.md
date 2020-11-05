# IMDB-API
A RESTful API service created for extracting movies data (something similar to IMDB)

# Requirements
Following are the requirements:
* Python version >= 3.8
* Django 3.1.2
* Also refer to requirements.txt

# Installation
1. clone desired directory with git clone https://github.com/subhakr11droy/IMDB-API.git
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

| Title | API Endpoints | Links |
| --- | --- | --- |
| API Overview | /api/ | https://imdbmovieapi.herokuapp.com/api/ |
| View all Movies | /api/movies/ | https://imdbmovieapi.herokuapp.com/api/movies |
| View All Genres | /api/genres/ | https://imdbmovieapi.herokuapp.com/api/genres/ |
| Single movie detail | /api/movie/{id} | https://imdbmovieapi.herokuapp.com/api/movie/1 |
| Search by movie | /api/movies?search={movie-name} | https://imdbmovieapi.herokuapp.com/api/movies/?search=Star%20Wars |
| Search by genre | /api/movies?search={genre-name} | https://imdbmovieapi.herokuapp.com/api/movies/?search=Action |
| Search by field | /api/movies?search={director-name} | https://imdbmovieapi.herokuapp.com/api/movies/?search=Steven%20Spielberg |
| Search with multi-field | /api/movies?search={movie-name},{director-name},{genre-name},... | https://imdbmovieapi.herokuapp.com/api/movies/?search=star,action |
| Search with Pagination | /api/movies?search=<movie-name>&limit=<#> | https://imdbmovieapi.herokuapp.com/api/movies/?search=star&limit=1

# How to scale the application?
Since, it completely depends on the scenario and requirements and a lot of factors are to be considered before coming up with an approach

Following can be done to scale the application, looking at the current requirements

* Infrastructure scaling
    1. Since the API plays a very crucial role in data retrieval of data, so api can be split up into different microservices
    3. Use of asynchronous server
    4. More application servers to serve requests in round-robin manner
    2. We can follow load balancing
    5. Use of consistent hashing for cashing servers

* Database scaling
    1. In case of 15 million API requests/day our database is more READ intensive, hence we can go for a non-relational db like NOSQL
    2. Any non-relational db like MongoDb offers high consistency and partition tolerance hence latency is low
    3. Profiling our queries
    4. Persistent connection on databases
    5. Searching for correct search key and indexing all the queries
    6. Analyzing the frequent queries and caching the queries
    7. Horizontal scaling of our databases

* Scaling the application and data transfer 
    1. We can completely avoid the unused middlewares and other non necessary apps in django
    2. Use of GraphQL
        * One of the major advantages of GraphQL over REST is clients have the ability to dictate exactly what they need from the server, and receive that data in a predictable way.
        * Rest on the other hand returns a complete object for each query
        * This helps in minimizing load on data transfer
