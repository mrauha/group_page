from django.db import models

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Article(models.Model):
    doi = models.CharField(max_length=200) # doi, url is created automatically from this
    url = "http://doi.org/{}".format(doi)
    authors = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    journal = models.CharField(max_length=200)
    pages_and_volume = models.CharField(max_length=200)
    year = models.DateField(
            default=timezone.now)
    description = models.TextField() # Abstract eg
    #image = models.ImageField(upload_to="article_images/") 
    status = models.CharField(max_length=300) # Submitted, being reviewed, published
    def __str__(self):
        return self.title