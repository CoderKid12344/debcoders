from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200, default="Title")
    desc = models.TextField()
    category = models.CharField(max_length=200, default="No Category")
    timestamp = models.DateTimeField(blank=True)
    slug = models.CharField(max_length=100, default="None")

    def __str__(self):
        return f"{self.title}"

class Contact(models.Model):
    username = models.CharField(max_length=200, default="None")
    email = models.EmailField()
    query = models.TextField()