from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Cart,CartItem
from rest_framework.response import Response
from rest_framework import status
from .serializers import CartSerializer,CartItemSerializer
from products.models import Product

# Create your views here.
class CartView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        # get or create the cart for logged in user
        # by authenticated user and the get user is correct or not then it will get or create based on that as true or falsr for cart and created
        cart , created = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)


class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')

        if not product_id:
            return Response({'error':'product_id is required'})
        if not quantity:
            return  Response({'error': 'quantity is required'})
        
        # get the product
        product = get_object_or_404(Product,id=product_id,is_active=True)

        # get the cart
        cart, _ = Cart.objects.get_or_create(user=request.user)

        # get or creating cart item
        item, created = CartItem.objects.get_or_create(cart=cart,product=product)

        if not created: # quantity is already exists
            item.quantity += int(quantity)
            item.save()

        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ManageCartView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self,request,item_id):
        # validate
        if 'change' not in request.data:
            return Response({"error":"Provide 'change' value"})
        
        change = int(request.data.get("change"))

        item = get_object_or_404(CartItem,pk=item_id, cart__user=request.user)
        product = item.product

        # for adding and checing the stock
        if change > 0:
            if item.quantity + change > product.stock:
                return Response({'error':'Not enough Stock'})
            
        new_qty = item.quantity + change
        # change can be +1 or -1
        
        if new_qty <=0:
            # remove the cart
            item.delete()
            return Response({'Success': "Item is removed"})
        
        # save the quantity
        item.quantity = new_qty
        item.save()
        serializer = CartItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)

