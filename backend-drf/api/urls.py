from django.urls import path
from users import views as Userviews
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from products import views as ProductViews
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
    
]