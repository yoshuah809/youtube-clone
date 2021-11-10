from django.http.response import Http404
from django.shortcuts import render
from .models import Comment, CommentReply
from .serializers import CommentSerializer, CommentReplySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status



class CommentList(APIView):

    def get(self, request):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):

    def get_object(self,pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self,request,pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

#Comment-Reply Views
class CommentReplyList(APIView):

    def get(self, request):
        comment = CommentReply.objects.all()
        serializer = CommentReplySerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentReplySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class CommentReplyDetail(APIView):

    def get_object(self,pk):
        try:
            return CommentReply.objects.get(pk=pk)
        except CommentReply.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        comment = self.get_object(pk)
        serializer = CommentReplySerializer(comment)
        return Response(serializer.data)

    def put(self,request,pk):
        comment = self.get_object(pk)
        serializer = CommentReplySerializer(comment, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)        
