from django.db import models
from django.utils import timezone
from user.models import User 


# Create your models here.

class Portfolio(models.Model):
    # editor = models.ForeignKey(User, on_delete = models.CASCADE)
    editor = models.CharField(max_length=100)
    title = models.CharField(max_length = 100)
    content = models.TextField()
    production = models.CharField(max_length=20)
    profile = models.ImageField(blank = True)
    grade = models.IntegerField()
    price = models.CharField(max_length = 20)

    def __str__(self):
        return self.title

class Review(models.Model):
    # writer = models.ForeignKey(User, on_delete = models.CASCADE)
    writer = models.CharField(max_length=100)
    content = models.TextField()
    grade = models.IntegerField()
    published_date = models.DateTimeField(default = timezone.now)
    portfolio = models.ForeignKey(Portfolio, on_delete = models.CASCADE)

    def __str__(self):
        return self.writer