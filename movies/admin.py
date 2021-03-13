from django.contrib import admin
from movies.models import Movies,Categories
# Register your models here.
admin.site.register(Movies)
admin.site.register(Categories)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title")