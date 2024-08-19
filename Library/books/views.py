from rest_framework import viewsets
from books.models import Books
from books.serializers import BookSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from books.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import generics

class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
