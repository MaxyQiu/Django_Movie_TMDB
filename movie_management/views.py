from django.shortcuts import render
from django.http import HttpResponse
from movie_management.models import Movie, Genre
from rest_framework.decorators import api_view
# Create your views here.

def filter_movies(request,genre):
    
    genre_id= Genre.objects.filter(genre=genre)[0].genre_id
    queryset = Movie.objects.filter(genre_ids__contains=genre_id)

    return render(request,'home.html',{'movies':queryset})

def sort_movies(request, feature):
    queryset= Movie.objects.order_by(feature)
    return render(request,'home.html',{'movies':queryset})

def update_movie_rating(request, id, new_data):
    #deal with different data type
   
      
    Movie.objects.filter(id=id).update(rating=new_data)
    

def add_movie(request, id, title ):
    movie=Movie.objects.create(id=id,title=title)
    return render(request,'home.html',{'movies':movie})

def delete_movie(request,id):
    Movie.objects.filter(id=id).delete()


@api_view
def bookmarked_movies(request):
   return 


