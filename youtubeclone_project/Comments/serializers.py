from rest_framework import serializers
from .models import Comment, CommentReply


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['video_id', 'comment', 'comment_likes', 'comment_dislikes']

class CommentReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentReply
        ields = ['comment', 'comment_reply']