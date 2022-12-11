from turtle import title
from unicodedata import category
from django.shortcuts import render,get_object_or_404
from .models import Actors, Category, Directors, Film, Scriptwriter, Studio
from series.models import Serie
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator
from comment.models import Comment
from comment.forms import CommentForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from accounts.models import Customer
# Create your views here.

def home(request):
    recentfilms = Film.objects.order_by('-created')[:6]

    recentseries = Serie.objects.order_by('-created')[:6]
    topratefilms = Film.objects.order_by('-rate')[:6]
    toprateseries = Serie.objects.order_by('-rate')[:6]
    newerfilms = Film.objects.order_by('-releaseyear')[:6]
    newerseries = Serie.objects.order_by('-releaseyear')[:6]
    likedfilms = Film.objects.order_by('-likes')[:6]
    likedseries = Serie.objects.order_by('-likes')[:6]
    if request.user.is_authenticated:
        user = request.user
        watchlist = Customer.objects.get(user=user)
    else:
        watchlist = Film.objects.order_by('-rate')[:6]

    
    
    
    context= {
        'recentfilms': recentfilms,
        'recentseries': recentseries,
        'topratefilms': topratefilms,
        'toprateseries': toprateseries,
        'newerfilms': newerfilms,
        'newerseries': newerseries,
        'likedfilms': likedfilms,
        'likedseries': likedseries,
        'watchlist': watchlist,
        
        
        
    }
    return render(request,'pages/home.html',context)


def filmcatalog(request):
    films = Film.objects.order_by('-created')   
    movierate = Film.objects.values_list('rate', flat=True).distinct()
    releaseyear=Film.objects.values_list('releaseyear', flat=True).distinct()
    paginator=Paginator(films ,4)
    page= request.GET.get('page')
    pagedfilms= paginator.get_page(page)
    
    
    context= {
        'pagedfilms': pagedfilms,
        'films': films,
        'movierate': movierate,
        'releaseyear': releaseyear,
        
        
    }
    return render(request,'pages/filmcatalog.html',context)

def catalog(request,category_slug=None):
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        films  = Film.objects.filter(category=categories).order_by('-created') 
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
    return render(request,'pages/filmcatalog.html',context)





def filmdetail(request,id):
    filmoneri = Film.objects.all()
    
    filmquery=get_object_or_404(Film, id=id)
    user = request.user
    comments = Comment.objects.filter(post=filmquery).order_by('date')

    if request.method == 'POST':
        forms = CommentForm(request.POST)
        if forms.is_valid():
            comment = forms.save(commit=False)
            comment.post = filmquery
            comment.user = user
            comment.save()
            return HttpResponseRedirect(reverse('filmdetail', args=[id]))
    else:
        forms = CommentForm()
    
    context= {
        'filmquery': filmquery,
        'filmoneri': filmoneri,
        'comments': comments,
        'forms':forms,
        
    }
    return render(request,'detail/filmdetail.html',context)



    

   
def actordetail(request,category_slug=None):
    portsquery=get_object_or_404(Actors, slug=category_slug)
    actordetail=Film.objects.filter(actors=portsquery)
    
    paginator=Paginator(actordetail ,6)
    page= request.GET.get('page')
    pagedfilms= paginator.get_page(page)
    
    
    context= {
        'actordetail':actordetail,
        'portsquery':portsquery,
        'pagedfilms':pagedfilms,
        
    }
    return render(request,'detail/actordetail.html',context)
    


def directordetail(request,category_slug=None):
    portsquery=get_object_or_404(Directors, slug=category_slug)
    directordetail=Film.objects.filter(directors=portsquery)
    paginator=Paginator(directordetail ,6)
    page= request.GET.get('page')
    pagedfilms= paginator.get_page(page)
    
    
    context= {
        'directordetail':directordetail,
        'portsquery':portsquery,
        'pagedfilms':pagedfilms,
        
    }
    return render(request,'detail/directordetail.html', context)

def writerdetail(request,category_slug=None):
    portsquery=get_object_or_404(Scriptwriter, slug=category_slug)
    writerdetail=Film.objects.filter(scriptwriter=portsquery)
    paginator=Paginator(writerdetail ,6)
    page= request.GET.get('page')
    pagedfilms= paginator.get_page(page)
    
    
    context= {
        
        'portsquery':portsquery,
        'pagedfilms':pagedfilms,
        
    }
    return render(request,'detail/writerdetail.html', context)

def studiodetail(request,category_slug=None):
    portsquery=get_object_or_404(Studio, slug=category_slug)
    studiodetail=Film.objects.filter(studio=portsquery)
    paginator=Paginator(studiodetail ,6)
    page= request.GET.get('page')
    pagedfilms= paginator.get_page(page)
    
    
    context= {
        
        'portsquery':portsquery,
        'pagedfilms':pagedfilms,
        
    }
    return render(request,'detail/studiodetail.html', context)

