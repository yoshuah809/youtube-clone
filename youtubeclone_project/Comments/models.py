from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Comment(models.Model):
    songId = models.CharField(max_length=50)
    comment= models.CharField(max_length=400)
    commentLikes =models.IntegerField(default=0) 
    commentDislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.comment