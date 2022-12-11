from .models import Categoryseries

def menu_links2(request):
    links2 = Categoryseries.objects.all()
    return dict(links2=links2)
