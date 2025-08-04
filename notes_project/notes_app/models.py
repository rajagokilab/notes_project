from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # owner
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # set on creation
    updated_at = models.DateTimeField(auto_now=True)      # update on save

    def __str__(self):
        return self.title
