from django.db import models


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=1024, null=False)
    category = models.CharField(max_length=64)
    content = models.TextField()
    timestamp = models.DateTimeField()
    url = models.URLField()

    def __str__(self):
        return self.title


class Template(models.Model):
    name = models.CharField(max_length=256, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.name
