from django.db import models

# Create your models here.
class Categories(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Movies(models.Model):
    title=models.CharField(max_length=50)
    overview = models.CharField(max_length=500)
    date=models.DateField(blank=True)
    poster=models.ImageField(upload_to="movies/posters")
    video=models.FileField(upload_to="movies/poster")
    categories =models.ManyToManyField(Categories)
    def __str__(self):
        return self.title
class ApiTest(models.Model):
    name=models.CharField(max_length=50)
    age = models.IntegerField