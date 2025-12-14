from django.urls import path
from users import views as Userviews
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from products import views as ProductViews
from carts import views as CartViews
from orders import views as OrdersViews

urlpatterns = [
    path('register/', Userviews.RegisterView.as_view()),

    # User API's
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', Userviews.ProfileView.as_view()),

    # product APIs
    # product list
    path("products/",ProductViews.ProductListView.as_view()),

    # product detail
    path("products/<int:pk>/",ProductViews.ProductDetailView.as_view()),
    
    # cart API
    path("cart/", CartViews.CartView.as_view()),

    # Add to cart
    path("cart/add", CartViews.AddToCartView.as_view()),

    # Manage cart
    path("cart/items/<int:item_id>/",CartViews.ManageCartView.as_view()),

    # order
    path("orders/place/",OrdersViews.PlaceOrderView.as_view())
]