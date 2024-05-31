from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    author = models.ForeignKey(User, related_name='posts', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tag
    # category
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_datetime = models.DateTimeField(null=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_datetime']
        
    def __str__(self):
        return self.title
    
    
    