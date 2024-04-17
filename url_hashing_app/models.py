from django.db import models

class Link(models.Model):
    full_address = models.TextField()
    key = models.CharField(max_length=10, unique=True)
    access_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)