from django.urls import path


from . import views
from .views import home,filmdetail
urlpatterns = [
    
    path('', views.home, name='home'),
    path('movies/', views.filmcatalog, name='filmcatalog'),
    
    path('movie/<int:id>/',views.filmdetail, name='filmdetail'),
    path('movie/<slug:category_slug>/',views.catalog, name='catalog'),
    
    #path('actor/', views.actordetail, name='actordetail'),
    path('actor/<slug:category_slug>/',views.actordetail, name='actordetail'),
    path('director/<slug:category_slug>/',views.directordetail, name='directordetail'),
    path('writer/<slug:category_slug>/',views.writerdetail, name='writerdetail'),
    path('studio/<slug:category_slug>/',views.studiodetail, name='studiodetail'),
    #path('', CourseListView.as_view(), name='courselist'),
   
   
     

] 
