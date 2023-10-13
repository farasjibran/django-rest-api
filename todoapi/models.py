from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(max_length=500)
  user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
  timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)

  def __str__(self):
    return self.title
