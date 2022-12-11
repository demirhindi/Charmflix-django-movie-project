from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

from django.urls import reverse
from .validators import file_size
from django.urls import reverse
from movies.models import Actors,Directors,Scriptwriter,Studio



class Categoryseries(models.Model):
    title = models.CharField(max_length=150,blank=True)
    slug = models.SlugField(max_length=150,unique=True,blank=True)
    

    class Meta:
        verbose_name='categoryserie'
        verbose_name_plural='categoriesserie'

    def get_url(self):
        return reverse('scatalog',kwargs={"category_slug":self.slug})

    def __str__(self):
        return self.title


class Serie(models.Model):
    name = models.CharField(max_length=150,blank=True)    
    category=models.ManyToManyField(Categoryseries,related_name="series")
    slug = models.SlugField(max_length=150,blank=True)    
    rate = models.FloatField(default=0)  
    releaseyear = models.IntegerField(default=2000,blank=True)    
    country = models.CharField(max_length=150,blank=True)
    actors=models.ManyToManyField(Actors,blank=True)
    directors=models.ManyToManyField(Directors,blank=True)
    scriptwriter=models.ManyToManyField(Scriptwriter,blank=True)
    studio=models.ManyToManyField(Studio,blank=True)
    thumbnail = models.ImageField(upload_to="series/thumbnails",blank=True)    
    desciption=models.TextField(max_length=20000,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    is_published=models.BooleanField(default=True)   
    likes = models.IntegerField(default=0)   

    class Meta:
        verbose_name='serie'
        verbose_name_plural='series'


    def get_url(self):
        return reverse('seriedetail',kwargs={"category_slug":self.slug}) 

    def __str__(self):
        return self.name

    @property
    def seasons(self):
        return self.seasons_set.all().order_by('id')

class Season(models.Model):
    name = models.CharField(max_length=150,blank=True)  
    serie=models.ForeignKey(Serie,related_name="seasons",on_delete=models.CASCADE)  
    slug = models.SlugField(max_length=150,blank=True)    
    thumbnail = models.ImageField(upload_to="series/seasons/thumbnails",blank=True)    
    desciption=models.TextField(max_length=20000,blank=True)
    created=models.DateTimeField(auto_now_add=True)
       

    def __str__(self):
        return self.name

    @property
    def episodes(self):
        return self.episodes_set.all().order_by('id')

class Episode(models.Model):
    name = models.CharField(max_length=150,blank=True) 
    epinumber=models.IntegerField(default=1,blank=True) 
   
    slug = models.SlugField(max_length=150,blank=True)  
    season=models.ForeignKey(Season,related_name="episodes",on_delete=models.CASCADE)  
    thumbnail = models.ImageField(upload_to="series/episodes/thumbnails",blank=True)    
    desciption=models.TextField(max_length=20000,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    video=models.FileField(upload_to="movie/%y",validators=[file_size],blank=True)  

    def get_url(self):
        return reverse('episode', args=[self.season.serie.slug, self.season.slug, self.slug])  
       

    def __str__(self):
        return self.name


def pre_save_categoryseries(sender,instance,*args, **kwargs):
    if not instance.slug:
        instance.slug=slugify(instance.title)

pre_save.connect(pre_save_categoryseries,sender=Categoryseries)

def pre_save_serie(sender,instance,*args, **kwargs):
    if not instance.slug:
        instance.slug=slugify(instance.name)

pre_save.connect(pre_save_serie,sender=Serie)

def pre_save_season(sender,instance,*args, **kwargs):
    if not instance.slug:
        instance.slug=slugify(instance.name)

pre_save.connect(pre_save_season,sender=Season)

def pre_save_episode(sender,instance,*args, **kwargs):
    if not instance.slug:
        instance.slug=slugify(instance.name)

pre_save.connect(pre_save_episode,sender=Episode)


