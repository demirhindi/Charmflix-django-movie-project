from django.contrib import admin

# Register your models here.
from .models import Categoryseries,Season,Serie,Episode

admin.site.register(Categoryseries)
admin.site.register(Episode)
admin.site.register(Season)
admin.site.register(Serie)



