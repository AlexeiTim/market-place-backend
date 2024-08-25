from rest_framework import serializers
from products.serializers import UserSerializer
from blog import models


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = models.Post
        fields = '__all__'
        