from rest_framework import serializers
from .models import Books
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, queryset=Books.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'books']

class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Books
    fields = '__all__'
    owner = UserSerializer(read_only=True)