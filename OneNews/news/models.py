from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=150)
    tags = models.CharField(max_length=1000)
    news_text = models.CharField(max_length=1000)
    source = models.CharField(max_length=150)   


