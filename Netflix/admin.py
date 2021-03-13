from django.contrib import admin
from Netflix.models import Movies,Categories
# Register your models here.
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title","overview","date")
admin.site.register(Movies,TaskAdmin)
admin.site.register(Categories)
