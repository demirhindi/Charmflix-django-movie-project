from django.shortcuts import render,get_object_or_404
from .models import Serie,Season,Categoryseries,Episode
from movies.models import Film
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator
from django.db.models import Count
from django.db.models import Q
# Create your views here.




def seriecatalog(request):
    serie = Serie.objects.order_by('-created')   
    movierate = Serie.objects.values_list('rate', flat=True).distinct()
    releaseyear=Serie.objects.values_list('releaseyear', flat=True).distinct()
    paginator=Paginator(serie ,4)
    page= request.GET.get('page')
    pagedfilms= paginator.get_page(page)
    
    
    context= {
        'pagedfilms': pagedfilms,
        'serie': serie,
        'movierate': movierate,
        'releaseyear': releaseyear,
        
        
    }
    return render(request,'pages/seriecatalog.html',context)

def scatalog(request,category_slug=None):
    if category_slug != None:
        categories = get_object_or_404(Categoryseries, slug=category_slug)
        films  = Serie.objects.filter(category=categories).order_by('-created') 
        paginator=Paginator(films ,4)
        page= request.GET.get('page')
        pagedfilms= paginator.get_page(page)
     
    movierate = Film.objects.values_list('rate', flat=True).distinct()
    releaseyear=Film.objects.values_list('releaseyear', flat=True).distinct()
    
    
    
    context= {
        'pagedfilms': pagedfilms,
        'films': films,
        'movierate': movierate,
        'releaseyear': releaseyear,
        
        
    }
    return render(request,'pages/seriecatalog.html',context)

def seriedetail(request,category_slug=None):
    
    
    filmquery=get_object_or_404(Serie, slug=category_slug)    
    filmoneri = Season.objects.filter(serie=filmquery)    
    sesononeri = Episode.objects.filter(season__serie=filmquery)
    

    print(sesononeri)

    
    context= {
        'filmquery': filmquery,
        'filmoneri': filmoneri,
        'sesononeri': sesononeri,
        
    }
    return render(request,'detail/seriedetail.html',context)


def episode(request,category_slug, season_slug, episode_slug):
    
    episodeinfo = Episode.objects.get(season__serie__slug=category_slug,season__slug=season_slug, slug=episode_slug)

    context= {
        'episodeinfo': episodeinfo,
        
    }
    return render(request,'detail/episode.html',context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            films= Film.objects.order_by('-created').filter( Q(name__icontains=keyword))
            film_count = films.count()
            
            series= Serie.objects.order_by('-created').filter( Q(name__icontains=keyword))
            series_count = series.count()
           
    context = {
        'films':films,
        'film_count': film_count,
        'series':series,
        'series_count': series_count,


    }
    return render(request,'pages/home.html',context)




