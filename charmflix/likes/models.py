from django.db import models
from movies.models import Film
from django.contrib.auth.models import User
from series.models import Serie
# Create your models here.

class Likesmovie(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
	post = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='post_like')

class Likesserie(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='serie_user_like')
	post = models.ForeignKey(Serie, on_delete=models.CASCADE, related_name='serie_post_like')