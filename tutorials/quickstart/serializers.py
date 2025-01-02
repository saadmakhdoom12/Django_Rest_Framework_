from django.contrib.auth.models import User
from quickstart.models import Snippet
from rest_framework import serializers


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ["id", "title", "code", "linenos", "language", "style"]
        owner = serializers.ReadOnlyField(source="owner.username")


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Snippet.objects.all()
    )

    class Meta:
        model = User
        fields = ["id", "username", "snippets"]
