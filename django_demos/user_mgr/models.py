from django.db import models
from django.contrib.auth.models import  User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    '''
    '''
    title = models.CharField(max_length=80)
    subtitle = models.CharField(max_length=120)
    publish_date = models.DateTimeField()
    content = models.TextField()
    link = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

