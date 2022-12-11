from django.shortcuts import render
from movies.models import Film
from accounts.models import Customer
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from series.models import Serie
# Create your views here.


@login_required
def favorite(request, id):
	user = request.user
	post = Film.objects.get(id=id)
	profile = Customer.objects.get(user=user)

	if profile.favorites.filter(id=id).exists():
		profile.favorites.remove(post)

	else:
		profile.favorites.add(post)

	return HttpResponseRedirect(reverse('filmdetail', args=[id]))

@login_required
def favoriteseries(request, category_slug=None):
	user = request.user
	post = Serie.objects.get(slug=category_slug)
	profile = Customer.objects.get(user=user)

	if profile.favoritesseries.filter(slug=category_slug).exists():
		profile.favoritesseries.remove(post)

	else:
		profile.favoritesseries.add(post)

	return HttpResponseRedirect(reverse('seriedetail', args=[category_slug]))