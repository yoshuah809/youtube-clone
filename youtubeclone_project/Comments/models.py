from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Comment(models.Model):
    video_id = models.CharField(max_length=50)
    comment= models.CharField(max_length=400)
    comment_likes =models.IntegerField(default=0) 
    comment_dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.comment

class CommentReply(models.Model):
    comment = models.ForeignKey('Comment', blank=True, null=True, on_delete=models.CASCADE)      
    comment_reply = models.CharField(max_length=400)