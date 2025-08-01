from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Post, Vote


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ("id", "value", "user", "post")
        read_only_fields = ("user",)


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    votes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ("id", "title", "content", "author", "created_at", "votes")

    def get_votes(self, obj):
        return sum(vote.value for vote in obj.votes.all())
