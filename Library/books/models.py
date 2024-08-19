from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

class Books(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  release_year = models.IntegerField()
  genre = models.CharField(max_length=50)
  pages = models.IntegerField()
  publish_company = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  owner = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)

  class Meta:
        ordering = ['created_at']