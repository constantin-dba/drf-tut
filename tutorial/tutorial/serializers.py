from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet

class UserSnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ["id", "title"]

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]

class UserDetailSerializer(serializers.ModelSerializer):
    snippets = UserSnippetSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "snippets"]

