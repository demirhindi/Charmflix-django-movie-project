from django.db import models
from movies.models import Film
from django.contrib.auth.models import User 

class Comment(models.Model):
	post = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='comments')
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)