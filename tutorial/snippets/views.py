from rest_framework.response import Response
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from snippets.serializers import SnippetSerializer
from rest_framework import generics
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class SnippetOptions(generics.GenericAPIView):
    """
    Возвращает все возможные значения для полей language и style
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get(self, request, *args, **kwargs):
        return Response({
            'language': [
                {'value': value, 'label': label} 
                for value, label in LANGUAGE_CHOICES
            ],
            'style': [
                {'value': value, 'label': label} 
                for value, label in STYLE_CHOICES
            ]
        })