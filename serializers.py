from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DDUser
        fields = ('name','avatar', 'id', 'bio')

class IssueSerializer(serializers.ModelSerializer):
    author = UserSerializer(source='author')
    class Meta:
        model = Issue
        fields = ('name', 'author', 'text', 'thresshold', 'positive', 'negative', 'neutral', 'id') 


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('issue', 'category', 'author', 'content', 'id', 'vote_up', 'vote_down', 'id')

class RelatedLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatedLink
        fields = ('issue', 'author', 'content', 'id', 'vote_up', 'vote_down', 'id')
