from django.urls import path
from . import views

urlpatterns=[

    path('filter_movies/<str:genre>/', views.filter_movies),
    path('sort_movies/<str:feature>/', views.sort_movies),
    path('add_movie/<int:id>/<str:title>/',views.add_movie),
    path('update_movie_rating/<int:id>/<str:new_data>/',views.update_movie_rating),
    path('delete_movie/<int:id>/<str:title>/',views.delete_movie),
    
]