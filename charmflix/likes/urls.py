

from django.urls import path


from . import views

urlpatterns = [
    
    
    path('movie/<int:id>/like/', views.like, name='postlike'),
    path('movie/<int:id>/dislike/', views.dislike, name='postdislike'),
    path('serie/<slug:category_slug>/like/', views.likeserie, name='postlikeserie'),
    path('serie/<slug:category_slug>/dislike/', views.dislikeserie, name='postdislikeserie'),


    
    

   
    
   
   
     

] 


