# models.py
from django.db import models


#{'adult': False, 'backdrop_path': '/zIYROrkHJPYB3VTiW1L9QVgaQO.jpg', 
# 'genre_ids': [28, 35], 'id': 897087, 'original_language': 'en', 
# 'original_title': 'Freelance',
#  'overview': 'An ex-special forces operative takes a job to 
# provide security for a journalist as she interviews a dictator, 
# but a military coup breaks out in the middle of the interview, 
# they are forced to escape into the jungle where they must survive.', 
# 'popularity': 2037.58, 'poster_path': '/7Bd4EUOqQDKZXA6Od5gkfzRNb0.jpg', 
# 'release_date': '2023-10-05', 
# 'title': 'Freelance', 'video': False, 'vote_average': 6.4, 'vote_count': 161}
class Movie(models.Model):
    movie_id= models.IntegerField(default=None)
    title = models.CharField(max_length=255)
    genre_ids = models.TextField(default="")
    release_date = models.DateField(null=True, blank=True)
    rating = models.FloatField(default=None)
    overview= models.TextField(default="")
    popularity= models.FloatField(default=None)
    bookmarked= models.BooleanField(default=False)
    # Add other fields as needed

class Genre(models.Model):
    genre_id= models.TextField(default="")
    genre= models.TextField()

class Details(models.Model):
    title = models.TextField()
    details= models.TextField()
    
# class BookMarked()