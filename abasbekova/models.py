from django.db import models

# Create your models here.
class addcard(models.Model):
    title = models.CharField(max_length=55)
    text = models.TextField(max_length=455)
    image = models.ImageField(upload_to="image")