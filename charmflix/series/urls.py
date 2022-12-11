from django.urls import path


from . import views
from .views import seriecatalog,seriedetail,episode
urlpatterns = [
    
    
    path('series/', views.seriecatalog, name='seriecatalog'),
    path('serie/<slug:category_slug>/',views.seriedetail, name='seriedetail'),
    path('series/<slug:category_slug>/',views.scatalog, name='scatalog'),
   #path('series/episode/', views.episode, name='episode'),
    path('serie/<slug:category_slug>/<slug:season_slug>/<slug:episode_slug>',views.episode, name='episode'),
    path('search/',views.search, name='search'),
    
   
   
     

] 
