from django.shortcuts import render
from rest_framework import viewsets

from .serializers import PostSerializer, GroupSerializer, CommentSerializer
from posts.models import Post, Group, Comment
# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    ...


class GroupViewSet(viewsets.ModelViewSet):
    ...


class CommentViewSet(viewsets.ModelViewSet):
    ...
