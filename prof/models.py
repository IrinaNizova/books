from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=20, blank=False, unique=True)
    title = models.CharField(max_length=30, blank=True)
    author = models.CharField(max_length=30, blank=False)
    description = models.CharField(max_length=512, blank=True)
    price = models.IntegerField(blank=False)

class Profile(models.Model):
    def __str__(self):
        return self.column_name
    column_name = models.TextField(editable=False)
    is_visible = models.BooleanField()