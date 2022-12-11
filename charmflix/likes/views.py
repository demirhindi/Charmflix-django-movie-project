from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from likes.models import Likesmovie,Likesserie
from movies.models import Film
from series.models import Serie
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def like(request, id):
	user = request.user
	post = Film.objects.get(id=id)
	current_likes = post.likes
	liked = Likesmovie.objects.filter(user=user, post=post).count()

	if not liked:
		like = Likesmovie.objects.create(user=user, post=post)
		like.save()
		current_likes = current_likes + 1

	        

    
	post.likes = current_likes
	post.save()
    

	return HttpResponseRedirect(reverse('filmdetail', args=[id]))

@login_required
def dislike(request, id):
	user = request.user
	post = Film.objects.get(id=id)
	current_likes = post.likes
	liked = Likesmovie.objects.filter(user=user, post=post).count()

	if liked:
		Likesmovie.objects.filter(user=user, post=post).delete()		
		current_likes = int(current_likes) - 1
    
	post.likes = current_likes
	post.save()
    

	return HttpResponseRedirect(reverse('filmdetail', args=[id]))

@login_required
def likeserie(request, category_slug=None):
	user = request.user
	post = Serie.objects.get(slug=category_slug)
	current_likes = post.likes
	liked = Likesserie.objects.filter(user=user, post=post).count()

	if not liked:
		like = Likesserie.objects.create(user=user, post=post)
		like.save()
		current_likes = current_likes + 1

	

    
	post.likes = current_likes
	post.save()
    

	return HttpResponseRedirect(reverse('seriedetail', args=[category_slug]))

@login_required
def dislikeserie(request, category_slug=None):
	user = request.user
	post = Serie.objects.get(slug=category_slug)
	current_likes = post.likes
	liked = Likesserie.objects.filter(user=user, post=post).count()


	if liked:
		Likesserie.objects.filter(user=user, post=post).delete()		
		current_likes = int(current_likes) - 1
    
	post.likes = current_likes
	post.save()
    

	return HttpResponseRedirect(reverse('seriedetail', args=[category_slug]))


