from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from carts.models import Cart
from .models import Order,OrderItem
from .serializers import OrderSerializer
from rest_framework import status
from .utils import send_order_notification
# Create your views here.
class PlaceOrderView(APIView):
    # the user is logged in 
    permission_classes = [IsAuthenticated]
    def post(self,request):
        #  check if order is empty
        cart = Cart.objects.get(user=request.user)
        if not cart or cart.items.count()==0:
            return Response({'Error':'Cart is empty'})
        # print("grand_total===>",cart.grand_total)
        # create the order
        order = Order.objects.create(
            user = request.user,
            subtotal = cart.subtotal,
            tax_amount = cart.tax_amount,
            grand_total = cart.grand_total
        )
        # create order items
        for item in cart.items.all():
            OrderItem.objects.create(
                order = order,
                product = item.product,
                quantity = item.quantity,
                price = item.product.price,
                total_price = item.total_price
            )
        # clear the cart items
        cart.items.all().delete()
        cart.save()
        # send the notification email
        send_order_notification(order)
        # return responce with status 201 to frontend
        serializer = OrderSerializer(order)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
