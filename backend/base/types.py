import graphene
from .models import Post,User
from graphene_django import DjangoObjectType
class PostType(DjangoObjectType):
    
    class Meta:
        model = Post
        fields = '__all__'
