from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

from django.urls import reverse
from .validators import file_size
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=150,blank=True)
    slug = models.SlugField(max_length=150,unique=True,blank=True)
    

    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('catalog',kwargs={"category_slug":self.slug})

    def __str__(self):
        return self.title

class Actors(models.Model):
    name = models.CharField(max_length=150,blank=True)
    slug = models.SlugField(max_length=150,blank=True)
    birthyear= models.IntegerField(default=2000,blank=True)
    bio=models.TextField(max_length=20000,blank=True)
    photo = models.ImageField(upload_to="actors/profile",blank=True)
    itfrom= models.CharField(max_length=150,blank=True)
    

    class Meta:
        verbose_name='actor'
        verbose_name_plural='actors'

    def get_url(self):
        return reverse('actordetail',kwargs={"category_slug":self.slug})

    def __str__(self):
        return self.name

class Directors(models.Model):
    name = models.CharField(max_length=150,blank=True)
    slug = models.SlugField(max_length=150,blank=True)
    birthyear= models.IntegerField(default=2000,blank=True)
    bio=models.TextField(max_length=20000,blank=True)
    photo = models.ImageField(upload_to="directors/profile",blank=True)
    itfrom= models.CharField(max_length=150,blank=True)
    

    class Meta:
        verbose_name='director'
        verbose_name_plural='directors'

    def get_url(self):
        return reverse('directordetail',kwargs={"category_slug":self.slug})

    def __str__(self):
        return self.name

class Scriptwriter(models.Model):
    name = models.CharField(max_length=150,blank=True)
    slug = models.SlugField(max_length=150,blank=True)
    birthyear= models.IntegerField(default=2000,blank=True)
    bio=models.TextField(max_length=20000,blank=True)
    photo = models.ImageField(upload_to="writer/profile",blank=True)
    itfrom= models.CharField(max_length=150,blank=True)
    

    class Meta:
        verbose_name='scriptwriter'
        verbose_name_plural='scriptwriters'

    def get_url(self):
        return reverse('writerdetail',kwargs={"category_slug":self.slug})

    def __str__(self):
        return self.name

class Studio(models.Model):
    name = models.CharField(max_length=150,blank=True)
    slug = models.SlugField(max_length=150,blank=True)
    sinceyear= models.IntegerField(default=2000,blank=True)
    desc=models.TextField(max_length=20000,blank=True)
    logo = models.ImageField(upload_to="studio/logo",blank=True)
    itfrom= models.CharField(max_length=150,blank=True)
    

    class Meta:
        verbose_name='Studio'
        verbose_name_plural='Studio'

    def get_url(self):
        return reverse('studiodetail',kwargs={"category_slug":self.slug})

    def __str__(self):
        return self.name


class Film(models.Model):
    name = models.CharField(max_length=150,blank=True)    
    category=models.ManyToManyField(Category,related_name="films")    
    rate = models.FloatField(default=0)  
    releaseyear = models.IntegerField(default=2000,blank=True)
    runningtime = models.IntegerField(default=10,blank=True)
    country = models.CharField(max_length=150,blank=True)
    actors=models.ManyToManyField(Actors,blank=True)
    directors=models.ManyToManyField(Directors,blank=True)
    scriptwriter=models.ManyToManyField(Scriptwriter,blank=True)
    studio=models.ManyToManyField(Studio,blank=True)
    thumbnail = models.ImageField(upload_to="movies/thumbnails",blank=True)    
    desciption=models.TextField(max_length=20000,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    is_published=models.BooleanField(default=True)
    video=models.FileField(upload_to="movie/%y",validators=[file_size],blank=True)
    likes = models.IntegerField(default=0)    


    def get_url(self):
        return reverse('filmdetail',kwargs={"id":self.id})

    def __str__(self):
        return self.name



def pre_save_category(sender,instance,*args, **kwargs):
    if not instance.slug:
        instance.slug=slugify(instance.title)

pre_save.connect(pre_save_category,sender=Category)

def pre_save_actors(sender,instance,*args, **kwargs):
    if not instance.slug:
        instance.slug=slugify(instance.name)

pre_save.connect(pre_save_actors,sender=Actors)

def pre_save_directors(sender,instance,*args, **kwargs):
    if not instance.slug:
        instance.slug=slugify(instance.name)

pre_save.connect(pre_save_directors,sender=Directors)

def pre_save_scriptwriter(sender,instance,*args, **kwargs):
    if not instance.slug:
        instance.slug=slugify(instance.name)

pre_save.connect(pre_save_scriptwriter,sender=Scriptwriter)

def pre_save_studio(sender,instance,*args, **kwargs):
    if not instance.slug:
        instance.slug=slugify(instance.name)

pre_save.connect(pre_save_studio,sender=Studio)

