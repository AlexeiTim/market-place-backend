from rest_framework import serializers
from orders import models



class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = models.Order
        fields = '__all__'
