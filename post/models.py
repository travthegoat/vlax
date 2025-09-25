from django.db import models
from uuid import uuid4

class Post(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    caption = models.TextField()
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.caption
    
    