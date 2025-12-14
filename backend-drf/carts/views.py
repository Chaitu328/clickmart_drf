from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Cart,CartItem
from rest_framework.response import Response
from rest_framework import status
from .serializers import CartSerializer
# Create your views here.
class CartView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        # get or create the cart for logged in user
        # by authenticated user and the get user is correct or not then it will get or create based on that as true or falsr for cart and created
        cart , created = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)