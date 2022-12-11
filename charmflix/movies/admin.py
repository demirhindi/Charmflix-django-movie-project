from django.contrib import admin

# Register your models here.
from .models import Category,Film,Actors,Directors,Scriptwriter,Studio

admin.site.register(Category)
admin.site.register(Film)
admin.site.register(Actors)
admin.site.register(Directors)
admin.site.register(Scriptwriter)
admin.site.register(Studio)


