from django.urls import path
from . import views

urlpatterns = [
    path('Comments/', views.CommentList.as_view()),
    path('Comments/<int:pk>', views.CommentDetail.as_view()),
    path('CommentsReply', views.CommentReplyList.as_view()),
]