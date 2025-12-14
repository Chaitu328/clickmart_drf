from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import OrderItem,Order

User = get_user_model()

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'