from rest_framework import serializers

from posts.models import Group, Post, Comment


class GroupSerializer(serializers.ModelSerializer):
    ...


class PostSerializer(serializers.ModelSerializer):
    ...


class CommentSerializer(serializers.ModelSerializer):
    ...
