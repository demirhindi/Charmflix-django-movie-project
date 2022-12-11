


from django.urls import path


from . import views

urlpatterns = [
    
    
    path('movie/<int:id>/favorite/', views.favorite, name='postfavorite'),
    path('serie/<slug:category_slug>/favorite/', views.favoriteseries, name='postfavoriteserie'),
    


    
    

   
    
   
   
     

] 





