from rest_framework import serializers
from .models import User,Post,Like
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'
class LikeSerializers(serializers.ModelSerializer):
    class Meta:
        model=Like
        fields='__all__'
        
        