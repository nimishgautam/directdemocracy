from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny
from django.shortcuts import render
from rest_framework import generics



#static views
def indexview(request):
    return render(request, 'index.html')

class UserViewSet(viewsets.ModelViewSet):
    queryset = DDUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = (AllowAny,)
    


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (AllowAny,)
    
    def get_queryset(self):
        queryset = Comment.objects.all()
        issue = self.request.QUERY_PARAMS.get('issue', None)
        if issue is not None:
            queryset = queryset.filter(issue__id=issue)
        return queryset
    

class RelatedLinkViewSet(viewsets.ModelViewSet):
    queryset = RelatedLink.objects.all()
    serializer_class = RelatedLinkSerializer
    permission_classes = (AllowAny,)
    
    def get_queryset(self):
        queryset = RelatedLink.objects.all()
        issue = self.request.QUERY_PARAMS.get('issue', None)
        if issue is not None:
            queryset = queryset.filter(issue__id=issue)
        return queryset
