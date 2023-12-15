from ast import literal_eval
from datetime import datetime
from django.core.management.base import BaseCommand
from movie_management.models import Movie, Genre
import requests
from django.conf import settings
import asyncio


class Command(BaseCommand):
    help = 'Populate movies from API'

    def handle(self, *args, **options):
        # Make API call to retrieve movie data
        #change the way we store api_key
        api_key= settings.API_KEY
        url_movie = "https://api.themoviedb.org/3/discover/movie"
        url_genre = "https://api.themoviedb.org/3/genre/movie/list"
        url_detail= "https://api.themoviedb.org/3/credit"
        params = {"api_key": api_key}
        response_genre_list = requests.get(url_genre, params=params)
        response_details = requests.get(url_detail, params=params)


        # Extract relevant data from the API response
        genre_list = response_genre_list.json().get("genres",[])
   
       # print(movie_list)

       # Populate the database with movie data
        page = 1
        has_more_data = True

        while has_more_data:
            # Make API call to retrieve movie data for the current page
            params = {"api_key": api_key, "page": page}
            response_movie_list = requests.get(url_movie, params=params)
            movie_list = response_movie_list.json().get("results", [])
            for movie_data in movie_list:
                release_date = movie_data.get("release_date")
                release_date= datetime.strptime(release_date, "%Y-%m-%d").date() if release_date else None
                Movie.objects.create(
                    movie_id=movie_data.get("id"),
                    title=movie_data.get("title"),
                    genre_ids=movie_data.get("genre_ids"),                   
                    rating = movie_data.get("vote_average"),
                    overview= movie_data.get("overview"),
                    popularity=movie_data.get("popularity"),
                    bookmarked= False,
                    # Add other fields as needed
                )
            has_more_data = len(movie_list) > 0
            page += 1

        #populate the database with genres data

        # for genre_data in genre_list:
        #     Genre.objects.create(
        #         genre_id= genre_data.get("id"),
        #         genre= genre_data.get("name")
        #     )
        
        #populate the database with movie details
        # async def fetch_movie_details(movie_id, api_key):
        # url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        # params = {"api_key": api_key}
        # response = await loop.run_in_executor(None, lambda: requests.get(url, params=params))
        # return response.json()
       
        # self.stdout.write(self.style.SUCCESS('Successfully populated movies'))