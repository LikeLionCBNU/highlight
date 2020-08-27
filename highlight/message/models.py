from django.db import models
from django.utils import timezone
# from user.models import User 

# Create your models here.

class Message(models.Model):
    # editor = models.ForeignKey(User, on_delete = models.CASCADE)
    # customer = models.ForeignKey(User, on_delete = models.CASCADE)
    editor = models.CharField(max_length=100)
    customer = models.CharField(max_length=100)
    content = models.TextField()
    send_date = models.DateTimeField(default=timezone.now)


