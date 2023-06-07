from django.shortcuts import render
from rest_framework import generics
from .models import User,Post,Like
from .serializers import UserSerializer,PostSerializer,LikeSerializer

class UserCreateAPIView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    
class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    
class PostCreateAPIView(generics.CreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    
class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    
class LikeCreateAPIView(generics.CreateAPIView):
    queryset=Like.objects.all()
    serializer_class=LikeSerializer
    
class LikeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Like.objects.all()
    serializer_class=LikeSerializer
# Create your views here.
